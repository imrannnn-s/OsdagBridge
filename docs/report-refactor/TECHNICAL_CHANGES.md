# OsdagBridge report generator — technical changes

## Scope
This change set refactors the PDF report path under `src/osdagbridge/core/reports` while preserving the existing report payload and bridge-design calculations.

## Implemented in source

1. **Long-table continuation headings** — `repeat_longtable_headers()` adds `\endfirsthead` / `\endhead` blocks to standard `longtable` tables that expose a bold column-heading row. Tables that already define continuation heads are left untouched.
2. **Page and table layout** — the report preamble uses a slightly tighter A4 page margin, explicit header/footer inclusion, consistent cell padding, row stretch, row height and rule width. The footer's large negative vertical adjustments were reduced to avoid collisions with body content.
3. **Separate live-load schedules** — Chapter 3 now prints separate vehicle-live-load and footway-live-load schedules. Vehicle choices come from the report input snapshot (the selected IRC/custom vehicle flags); footway mode and pressure are reported separately with units.
4. **Utilization charts** — Chapter 5 builds chart points from the calculated UR values used in the overall design-check summary and draws a red dashed UR=1.0 capacity line. Available values are grouped into girder, deck/slab, cross-bracing and end-diaphragm charts; unavailable categories are omitted rather than populated with invented values.
5. **Material charts** — Chapter 7 adds structural-steel quantity and concrete/reinforcement quantity charts using existing BOM quantity fields. Missing or nonnumeric source fields are omitted from chart series.
6. **Centralized style** — `styles.py` defines report theme values and `apply_report_style()` applies them to the assembled LaTeX document.

## Data limitations to understand

- The report generator currently exposes a limited set of quantity keys. The end-diaphragm steel bar uses `end_diaphragm_wt_total`; if the upstream BOM does not populate that field, the chart omits that bar.
- Concrete volume and reinforcement weight are different physical units. Their comparison chart labels both quantities and should be interpreted as a quantity overview, not a like-for-like magnitude comparison.
- End-diaphragm utilization is only charted when the design summary supplies a numeric UR (for example, when the configured diaphragm is designed through the bracing path). Unsupported design modes remain absent rather than showing fabricated values.
- The chart uses PGFPlots/TikZ packages supplied by a standard TeX Live / MiKTeX installation.

## Validation performed

- Python `compileall` over `src/osdagbridge`.
- Unit-style checks of continuation-header insertion and centralized style application.
- LaTeX smoke compilation of Chapters 3, 5 and 7 using sample / empty bridge data.
- A full GUI-driven PDF regression still needs to be run on the target Windows environment with the user's installed OsdagBridge conda environment and the actual design payload. The original 80-page baseline PDF is not regenerated or included as an altered output.


## Follow-up reliability corrections

- Added the missing `apply_report_style` import in `report_generator.py`.
- Removed the temporary-directory lifetime problem for report resources.
  Previously, the `.tex` file was copied out of a temporary directory after
  compilation while its relative `assets/...` references pointed to files that
  were deleted with that directory.
- Assets and generated figures are now stored alongside the report source in
  the report output directory, and compilation runs with that directory as
  its working directory.
- Added a persistent `<report>_compile.log` with stdout/stderr and pass status.
- Missing packaged Osdag logo is handled as an optional cover element.
