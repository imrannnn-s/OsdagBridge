"""Matplotlib chart generation for report figures."""

import os
import shutil
import tempfile

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt

from .styles import REPORT_STYLE


def _style_axes(ax):
    ax.grid(
        axis="y",
        color=REPORT_STYLE["chart_grid_color"],
        linewidth=REPORT_STYLE["chart_grid_line_width"],
    )
    ax.set_axisbelow(True)
    ax.tick_params(axis="both", labelsize=REPORT_STYLE["chart_tick_font_size"])


def _save_chart(fig, filename, assets_dir):
    os.makedirs(assets_dir, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="osdagbridge-report-chart-") as temp_dir:
        temp_path = os.path.join(temp_dir, filename)
        fig.savefig(
            temp_path,
            dpi=REPORT_STYLE["chart_dpi"],
            bbox_inches="tight",
            facecolor=REPORT_STYLE["chart_background_color"],
        )
        shutil.copy2(temp_path, os.path.join(assets_dir, filename))
    plt.close(fig)
    return os.path.join("assets", "images", filename).replace("\\", "/")


def create_ur_charts(charts, assets_dir):
    """Create one annotated PNG for each named UR chart and return TeX paths."""
    outputs = {}
    with plt.rc_context({
        "font.family": REPORT_STYLE["chart_font_family"],
        "font.size": REPORT_STYLE["chart_font_size"],
    }):
        for key, title, labels, values in charts:
            fig, ax = plt.subplots(figsize=REPORT_STYLE["ur_chart_size"])
            x_positions = list(range(len(values)))
            colors = [
                REPORT_STYLE["chart_pass_color"]
                if value <= REPORT_STYLE["ur_threshold"]
                else REPORT_STYLE["chart_fail_color"]
                for value in values
            ]
            bars = ax.bar(
                x_positions,
                values,
                width=REPORT_STYLE["ur_bar_width"],
                color=colors,
            )
            ax.axhline(
                REPORT_STYLE["ur_threshold"],
                color=REPORT_STYLE["chart_threshold_color"],
                linestyle="--",
                linewidth=REPORT_STYLE["chart_threshold_line_width"],
            )
            ymax = max(
                REPORT_STYLE["ur_min_ymax"],
                max(values) * REPORT_STYLE["ur_ymax_scale"] if values else 0,
            )
            ax.set_ylim(0, ymax)
            ax.set_xticks(x_positions, labels)
            ax.tick_params(
                axis="x",
                labelrotation=REPORT_STYLE["chart_rotation"],
                labelsize=REPORT_STYLE["chart_tick_font_size"],
            )
            for tick in ax.get_xticklabels():
                tick.set_horizontalalignment("right")
            ax.set_ylabel(
                "Utilization Ratio (Demand / Capacity)",
                fontsize=REPORT_STYLE["chart_axis_label_font_size"],
            )
            ax.set_title(title, fontsize=REPORT_STYLE["chart_title_font_size"])
            _style_axes(ax)
            if not values:
                ax.text(
                    0.5,
                    0.5,
                    "No utilization data available",
                    transform=ax.transAxes,
                    ha="center",
                    va="center",
                )
            for bar, value in zip(bars, values):
                ax.annotate(
                    f"{value:.2f}",
                    (bar.get_x() + bar.get_width() / 2, value),
                    xytext=(0, 4),
                    textcoords="offset points",
                    ha="center",
                    va="bottom",
                    fontsize=REPORT_STYLE["chart_value_font_size"],
                )
            fig.tight_layout()
            outputs[key] = _save_chart(fig, f"{key}.png", assets_dir)
    return outputs


def create_material_charts(steel_quantities, concrete_volume, rebar_weight, assets_dir):
    """Create separate steel and split-axis concrete/reinforcement PNG charts."""
    outputs = {}
    with plt.rc_context({
        "font.family": REPORT_STYLE["chart_font_family"],
        "font.size": REPORT_STYLE["chart_font_size"],
    }):
        labels = [label for label, _ in steel_quantities]
        known_values = [
            (index, value)
            for index, (_, value) in enumerate(steel_quantities)
            if value is not None
        ]
        fig, ax = plt.subplots(figsize=REPORT_STYLE["steel_chart_size"])
        if known_values:
            x_positions, values = zip(*known_values)
            bars = ax.bar(
                x_positions,
                values,
                width=REPORT_STYLE["quantity_bar_width"],
                color=REPORT_STYLE["chart_pass_color"],
            )
            for bar, value in zip(bars, values):
                ax.annotate(
                    f"{value:.2f}",
                    (bar.get_x() + bar.get_width() / 2, value),
                    xytext=(0, 4),
                    textcoords="offset points",
                    ha="center",
                    va="bottom",
                    fontsize=REPORT_STYLE["chart_value_font_size"],
                )
        else:
            values = ()
        ax.set_xticks(range(len(labels)), labels)
        ax.set_ylabel("Weight (MT)", fontsize=REPORT_STYLE["chart_axis_label_font_size"])
        ax.set_title("Structural Steel Quantities", fontsize=REPORT_STYLE["chart_title_font_size"])
        ax.tick_params(axis="x", labelrotation=REPORT_STYLE["chart_rotation"])
        for tick in ax.get_xticklabels():
            tick.set_horizontalalignment("right")
        _style_axes(ax)
        height = max(values, default=0) * REPORT_STYLE["ur_ymax_scale"]
        missing_y = height * 0.02 if height else REPORT_STYLE["ur_min_ymax"] * 0.02
        for index, label in enumerate(labels):
            if steel_quantities[index][1] is None:
                ax.text(index, missing_y, "N/A", ha="center", va="bottom")
        fig.tight_layout()
        outputs["material_steel"] = _save_chart(fig, "material_steel.png", assets_dir)

        fig, axes = plt.subplots(1, 2, figsize=REPORT_STYLE["quantity_chart_size"])
        for ax, title, ylabel, value in (
            (axes[0], "Concrete Volume", "Volume (m$^3$)", concrete_volume),
            (axes[1], "Reinforcement Steel", "Weight (MT)", rebar_weight),
        ):
            _style_axes(ax)
            ax.set_title(title, fontsize=REPORT_STYLE["chart_title_font_size"])
            ax.set_ylabel(ylabel, fontsize=REPORT_STYLE["chart_axis_label_font_size"])
            ax.set_xticks([0], [title])
            if value is None:
                ax.text(0.5, 0.5, "N/A", transform=ax.transAxes, ha="center", va="center")
                continue
            bar = ax.bar(
                [0],
                [value],
                width=REPORT_STYLE["quantity_bar_width"],
                color=REPORT_STYLE["chart_pass_color"],
            )[0]
            ax.annotate(
                f"{value:.2f}",
                (bar.get_x() + bar.get_width() / 2, value),
                xytext=(0, 4),
                textcoords="offset points",
                ha="center",
                va="bottom",
                fontsize=REPORT_STYLE["chart_value_font_size"],
            )
        fig.tight_layout()
        outputs["material_concrete_rebar"] = _save_chart(
            fig, "material_concrete_rebar.png", assets_dir
        )
    return outputs
