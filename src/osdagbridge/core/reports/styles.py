"""Centralized visual configuration for generated OsdagBridge design reports."""

REPORT_STYLE = {
    "page_margin": "0.82in",
    "header_height": "18pt",
    "footer_skip": "28pt",
    "table_column_padding": "5pt",
    "table_compact_column_padding": "4pt",
    "table_dense_column_padding": "3.5pt",
    "table_tight_column_padding": "3pt",
    "table_row_stretch": "1.16",
    "table_compact_row_stretch": "1.25",
    "table_extra_row_height": "1pt",
    "table_row_extra_space": "6pt",
    "table_rule_width": "0.45pt",
    "longtable_pre_skip": "0pt",
    "longtable_post_skip": "5pt",
    "longtable_needspace": "6\\baselineskip",
    "table_needspace": "6\\baselineskip",
    "figure_needspace": "26\\baselineskip",
    "footer_rule_gap": "0pt",
    "footer_rule_vspace": "6pt",
    "header_rule_width": "1pt",
    "header_rule_gap": "2pt",
    "footer_supplement_top": "-3pt",
    "footer_supplement_bottom": "4pt",
    "document_font_size": "12pt",
    "line_stretch": "1.15",
    "brand_green": "91B014",
    "failure_color": "B00020",
    "success_color": "008000",
    "blue_color": "0070C0",
    "black_color": "000000",
    "font_small": r"\small",
    "font_footnotesize": r"\footnotesize",
    "font_scriptsize": r"\scriptsize",
    "font_normal": r"\normalsize",
    "font_large": r"\large",
    "font_Large": r"\Large",
    "font_Huge": r"\Huge",
    "figure_width_full": r"\textwidth",
    "figure_width_summary": r"0.9\textwidth",
    "figure_width_analysis": r"0.75\textwidth",
    "figure_width_drawing": r"0.85\textwidth",
    "figure_width_placeholder": r"0.97\textwidth",
    "figure_width_minipage": r"0.31\textwidth",
    "figure_width_placeholder_box": r"0.95\linewidth",
    "figure_width_title_left": r"0.6\textwidth",
    "figure_width_title_right": r"0.35\textwidth",
    "figure_logo_height": "2.2cm",
    "figure_logo_width": r"\linewidth",
    "figure_embed_top_gap": "-0.5em",
    "figure_embed_bottom_gap": "0.5em",
    "figure_inner_padding": "4pt",
    "section_gap": "1em",
    "section_gap_tiny": "0.3em",
    "section_gap_small": "0.4em",
    "section_gap_medium": "0.6em",
    "section_gap_large": "0.8em",
    "section_gap_extra_large": "2.2em",
    "section_gap_small_cm": "0.4cm",
    "section_gap_medium_cm": "0.8cm",
    "section_gap_half_cm": "0.5cm",
    "title_gap": "2cm",
    "title_page_top_gap": "1.5cm",
    "title_page_gap_small": "0.3cm",
    "title_page_gap_medium": "1cm",
    "title_page_gap_large": "1.5cm",
    "chapter_label_gap": "1em",
    "chapter_title_indent": "0pt",
    "chapter_title_before": "0pt",
    "chapter_title_after": "10pt",
    "chapter_summary_before": "-30pt",
    "toc_chapter_indent": "1.5em",
    "toc_section_indent": "3.8em",
    "toc_subsection_indent": "7.0em",
    "toc_chapter_label_width": "1.5em",
    "toc_chapter_hspace": "-1.5em",
    "toc_section_label_width": "2.3em",
    "toc_section_hspace": "-2.3em",
    "toc_subsection_label_width": "3.2em",
    "toc_subsection_hspace": "-3.2em",
    "toc_chapter_gap": "2pt",
    "caption_skip": "2pt",
    "chart_dpi": 200,
    "chart_font_family": "DejaVu Sans",
    "chart_font_size": 9,
    "chart_tick_font_size": 8,
    "chart_value_font_size": 9,
    "chart_axis_label_font_size": 9,
    "chart_title_font_size": 10,
    "chart_rotation": 30,
    "ur_chart_size": (11.0, 5.2),
    "steel_chart_size": (10.5, 5.0),
    "quantity_chart_size": (11.0, 5.0),
    "ur_bar_width": 0.6,
    "quantity_bar_width": 0.6,
    "ur_threshold": 1.0,
    "ur_min_ymax": 1.2,
    "ur_ymax_scale": 1.15,
    "chart_pass_color": "#2E8B57",
    "chart_fail_color": "#C00020",
    "chart_threshold_color": "#C00020",
    "chart_grid_color": "#D9D9D9",
    "chart_background_color": "white",
    "chart_grid_line_width": 0.7,
    "chart_threshold_line_width": 1.5,
    "warning_color": "FFFF00",
}


def apply_report_style(tex: str) -> str:
    """Apply centralized values to the report's LaTeX preamble/layout."""
    replacements = {
        r"\documentclass[REPORT_DOCUMENT_FONT_SIZE,a4paper]{report}":
            rf"\documentclass[{REPORT_STYLE['document_font_size']},a4paper]{{report}}",
        r"margin=REPORT_PAGE_MARGIN": f"margin={REPORT_STYLE['page_margin']}",
        r"\setlength{\headheight}{REPORT_HEADER_HEIGHT}":
            rf"\setlength{{\headheight}}{{{REPORT_STYLE['header_height']}}}",
        r"\setlength{\footskip}{REPORT_FOOTER_SKIP}":
            rf"\setlength{{\footskip}}{{{REPORT_STYLE['footer_skip']}}}",
        r"\setstretch{REPORT_LINE_STRETCH}": rf"\setstretch{{{REPORT_STYLE['line_stretch']}}}",
        r"height REPORT_HEADER_RULE_WIDTH":
            f"height {REPORT_STYLE['header_rule_width']}",
        r"\vspace{-3pt}": rf"\vspace{{{REPORT_STYLE['footer_supplement_top']}}}",
        r"\vspace{4pt}": rf"\vspace{{{REPORT_STYLE['footer_supplement_bottom']}}}",
        r"\vspace{6pt}": rf"\vspace{{{REPORT_STYLE['footer_rule_vspace']}}}",
        r"\vspace{0pt}": rf"\vspace{{{REPORT_STYLE['footer_rule_gap']}}}",
        r"\vspace{REPORT_HEADER_RULE_GAP}":
            rf"\vspace{{{REPORT_STYLE['header_rule_gap']}}}",
        r"\vspace{REPORT_TOC_CHAPTER_GAP}":
            rf"\vspace{{{REPORT_STYLE['toc_chapter_gap']}}}",
        r"\setlength{\tabcolsep}{REPORT_TABLE_COLUMN_PADDING}":
            rf"\setlength{{\tabcolsep}}{{{REPORT_STYLE['table_column_padding']}}}",
        r"\renewcommand{\arraystretch}{REPORT_TABLE_ROW_STRETCH}":
            rf"\renewcommand{{\arraystretch}}{{{REPORT_STYLE['table_row_stretch']}}}",
        r"\setlength{\LTpre}{REPORT_LONGTABLE_PRE_SKIP}":
            rf"\setlength{{\LTpre}}{{{REPORT_STYLE['longtable_pre_skip']}}}",
        r"\setlength{\LTpost}{REPORT_LONGTABLE_POST_SKIP}":
            rf"\setlength{{\LTpost}}{{{REPORT_STYLE['longtable_post_skip']}}}",
        r"\setlength{\arrayrulewidth}{REPORT_TABLE_RULE_WIDTH}":
            rf"\setlength{{\arrayrulewidth}}{{{REPORT_STYLE['table_rule_width']}}}",
        r"\setlength{\extrarowheight}{REPORT_TABLE_EXTRA_ROW_HEIGHT}":
            rf"\setlength{{\extrarowheight}}{{{REPORT_STYLE['table_extra_row_height']}}}",
        r"\BeforeBeginEnvironment{table}{\needspace{REPORT_TABLE_NEEDSPACE}}":
            rf"\BeforeBeginEnvironment{{table}}{{\needspace{{{REPORT_STYLE['table_needspace']}}}}}",
        r"\BeforeBeginEnvironment{figure}{\needspace{REPORT_FIGURE_NEEDSPACE}}":
            rf"\BeforeBeginEnvironment{{figure}}{{\needspace{{{REPORT_STYLE['figure_needspace']}}}}}",
        r"\BeforeBeginEnvironment{longtable}{\needspace{REPORT_LONGTABLE_NEEDSPACE}}":
            rf"\BeforeBeginEnvironment{{longtable}}{{\needspace{{{REPORT_STYLE['longtable_needspace']}}}}}",
        r"\definecolor{osdagGreen}{HTML}{REPORT_BRAND_GREEN}": (
            rf"\definecolor{{osdagGreen}}{{HTML}}{{{REPORT_STYLE['brand_green']}}}" + "\n" +
            rf"\definecolor{{reportRed}}{{HTML}}{{{REPORT_STYLE['failure_color']}}}" + "\n" +
            rf"\definecolor{{reportBlue}}{{HTML}}{{{REPORT_STYLE['blue_color']}}}" + "\n" +
            rf"\definecolor{{reportBlack}}{{HTML}}{{{REPORT_STYLE['black_color']}}}" + "\n" +
            rf"\definecolor{{reportYellow}}{{HTML}}{{{REPORT_STYLE['warning_color']}}}" + "\n" +
            rf"\newcommand{{\ReportSmall}}{{{REPORT_STYLE['font_small']}}}" + "\n" +
            rf"\newcommand{{\ReportFootnotesize}}{{{REPORT_STYLE['font_footnotesize']}}}" + "\n" +
            rf"\newcommand{{\ReportScriptsize}}{{{REPORT_STYLE['font_scriptsize']}}}" + "\n" +
            rf"\newcommand{{\ReportLarge}}{{{REPORT_STYLE['font_large']}}}" + "\n" +
            rf"\newcommand{{\ReportTitleLarge}}{{{REPORT_STYLE['font_Large']}}}" + "\n" +
            rf"\newcommand{{\ReportTitleHuge}}{{{REPORT_STYLE['font_Huge']}}}" + "\n" +
            rf"\newcommand{{\ReportNormal}}{{{REPORT_STYLE['font_normal']}}}" + "\n" +
            rf"\newcommand{{\ReportTablePadding}}{{{REPORT_STYLE['table_column_padding']}}}" + "\n" +
            rf"\newcommand{{\ReportTablePaddingCompact}}{{{REPORT_STYLE['table_compact_column_padding']}}}" + "\n" +
            rf"\newcommand{{\ReportTablePaddingDense}}{{{REPORT_STYLE['table_dense_column_padding']}}}" + "\n" +
            rf"\newcommand{{\ReportTablePaddingTight}}{{{REPORT_STYLE['table_tight_column_padding']}}}" + "\n" +
            rf"\newcommand{{\ReportCompactArrayStretch}}{{{REPORT_STYLE['table_compact_row_stretch']}}}" + "\n" +
            rf"\newcommand{{\ReportFigureFullWidth}}{{{REPORT_STYLE['figure_width_full']}}}" + "\n" +
            rf"\newcommand{{\ReportFigureSummaryWidth}}{{{REPORT_STYLE['figure_width_summary']}}}" + "\n" +
            rf"\newcommand{{\ReportFigureAnalysisWidth}}{{{REPORT_STYLE['figure_width_analysis']}}}" + "\n" +
            rf"\newcommand{{\ReportFigureDrawingWidth}}{{{REPORT_STYLE['figure_width_drawing']}}}" + "\n" +
            rf"\newcommand{{\ReportFigurePlaceholderWidth}}{{{REPORT_STYLE['figure_width_placeholder']}}}" + "\n" +
            rf"\newcommand{{\ReportFigureMinipageWidth}}{{{REPORT_STYLE['figure_width_minipage']}}}" + "\n" +
            rf"\newcommand{{\ReportFigureLogoHeight}}{{{REPORT_STYLE['figure_logo_height']}}}" + "\n" +
            rf"\newcommand{{\ReportFigureLogoWidth}}{{{REPORT_STYLE['figure_logo_width']}}}" + "\n" +
            rf"\newcommand{{\ReportTableRowGap}}{{{REPORT_STYLE['table_row_extra_space']}}}" + "\n" +
            rf"\newcommand{{\ReportCaptionSkip}}{{{REPORT_STYLE['caption_skip']}}}"
        ),
        r"\colorbox{yellow}": r"\colorbox{reportYellow}",
        r"\begin{minipage}[c]{0.6\textwidth}":
            rf"\begin{{minipage}}[c]{{{REPORT_STYLE['figure_width_title_left']}}}",
        r"\begin{minipage}[c]{0.35\textwidth}":
            rf"\begin{{minipage}}[c]{{{REPORT_STYLE['figure_width_title_right']}}}",
        r"\vspace*{1.5cm}":
            rf"\vspace*{{{REPORT_STYLE['title_page_top_gap']}}}",
        r"\\[0.3cm]": rf"\\[{REPORT_STYLE['title_page_gap_small']}]",
        r"\\[1cm]": rf"\\[{REPORT_STYLE['title_page_gap_medium']}]",
        r"\\[1.5cm]": rf"\\[{REPORT_STYLE['title_page_gap_large']}]",
        r"{\thechapter}{1em}{}":
            rf"{{\thechapter}}{{{REPORT_STYLE['chapter_label_gap']}}}{{}}",
        r"\titlespacing*{\chapter}{0pt}{0pt}{10pt}":
            rf"\titlespacing*{{\chapter}}{{{REPORT_STYLE['chapter_title_indent']}}}"
            rf"{{{REPORT_STYLE['chapter_title_before']}}}"
            rf"{{{REPORT_STYLE['chapter_title_after']}}}",
        r"\titlespacing*{\chapter}{0pt}{-30pt}{10pt}":
            rf"\titlespacing*{{\chapter}}{{{REPORT_STYLE['chapter_title_indent']}}}"
            rf"{{{REPORT_STYLE['chapter_summary_before']}}}"
            rf"{{{REPORT_STYLE['chapter_title_after']}}}",
        r"\titlecontents{chapter}[1.5em]":
            rf"\titlecontents{{chapter}}[{REPORT_STYLE['toc_chapter_indent']}]",
        r"\titlecontents{section}[3.8em]":
            rf"\titlecontents{{section}}[{REPORT_STYLE['toc_section_indent']}]",
        r"\titlecontents{subsection}[7.0em]":
            rf"\titlecontents{{subsection}}[{REPORT_STYLE['toc_subsection_indent']}]",
        r"\contentslabel{1.5em}":
            rf"\contentslabel{{{REPORT_STYLE['toc_chapter_label_width']}}}",
        r"\hspace*{-1.5em}":
            rf"\hspace*{{{REPORT_STYLE['toc_chapter_hspace']}}}",
        r"\contentslabel{2.3em}":
            rf"\contentslabel{{{REPORT_STYLE['toc_section_label_width']}}}",
        r"\hspace*{-2.3em}":
            rf"\hspace*{{{REPORT_STYLE['toc_section_hspace']}}}",
        r"\contentslabel{3.2em}":
            rf"\contentslabel{{{REPORT_STYLE['toc_subsection_label_width']}}}",
        r"\hspace*{-3.2em}":
            rf"\hspace*{{{REPORT_STYLE['toc_subsection_hspace']}}}",
    }
    for old, new in replacements.items():
        tex = tex.replace(old, new)
    spacing_replacements = {
        r"\vspace{1em}": REPORT_STYLE["section_gap"],
        r"\vspace{0.3em}": REPORT_STYLE["section_gap_tiny"],
        r"\vspace{0.4em}": REPORT_STYLE["section_gap_small"],
        r"\vspace{0.6em}": REPORT_STYLE["section_gap_medium"],
        r"\vspace{0.8em}": REPORT_STYLE["section_gap_large"],
        r"\vspace{2.2em}": REPORT_STYLE["section_gap_extra_large"],
        r"\vspace{0.4cm}": REPORT_STYLE["section_gap_small_cm"],
        r"\vspace{0.8cm}": REPORT_STYLE["section_gap_medium_cm"],
        r"\vspace{0.5cm}": REPORT_STYLE["section_gap_half_cm"],
        r"\vspace{2cm}": REPORT_STYLE["title_gap"],
        r"\vspace{1.5cm}": REPORT_STYLE["title_page_top_gap"],
        r"\vspace{-0.5em}": REPORT_STYLE["figure_embed_top_gap"],
        r"\vspace{0.5em}": REPORT_STYLE["figure_embed_bottom_gap"],
    }
    for old, value in spacing_replacements.items():
        tex = tex.replace(old, rf"\vspace{{{value}}}")
    tex = tex.replace(r"\\[6pt]", r"\\[\ReportTableRowGap]")
    return tex
