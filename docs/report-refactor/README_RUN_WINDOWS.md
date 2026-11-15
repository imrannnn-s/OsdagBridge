# Run and record the OsdagBridge report demonstration (Windows)

## 1. Activate the existing environment
Open **Anaconda Prompt** and run:

```bat
conda activate osdagbridge-env
cd /d "%USERPROFILE%\Downloads\OsdagBridge-dev\OsdagBridge-dev"
```

If you extracted this ZIP somewhere else, change the `cd` path to that folder.

## 2. Install the modified source into the environment

```bat
python -m pip install -e .
```

The report generator also requires a working LaTeX distribution (`pdflatex`) with PGFPlots/TikZ available. Confirm with:

```bat
where pdflatex
kpsewhich pgfplots.sty
```

If either command fails, install/update MiKTeX or TeX Live and ensure its `bin` directory is on PATH.

## 3. Launch OsdagBridge

```bat
cd src
python -m osdagbridge.desktop
```

Create/open a plate-girder bridge design, run the design, then use **Generate Report**. Keep the same design inputs when comparing the baseline and updated report.

## 4. Record the demonstration

- Press `Win + G` to open Xbox Game Bar.
- Press `Win + Alt + R` to start/stop recording.
- Record the report generation, then open the resulting PDF and show the repeated table headings, separate load tables, utilization charts and quantity charts.
- Captures are normally saved under `Videos\Captures`.

For a submission video, show the GUI inputs first, click Generate Report, wait for compilation, then scroll through Chapters 3, 5 and 7.


## Report generation reliability fixes

The report generator now imports the centralized style helper explicitly and
keeps its TeX resources in the selected report output directory:

- `assets/osdag_logo.png` is copied from the packaged Osdag resource when present.
- Generated figures are retained under `assets/images/` and referenced using
  paths relative to the `.tex` file.
- The PDF is compiled with the output directory as its working directory.
- The `.tex`, assets, and `<report>_compile.log` remain available after a failed
  compilation, making diagnosis reproducible.
- The Osdag logo is optional: if the packaged file is unavailable, the cover
  displays a text placeholder instead of failing compilation.

After installing the updated project in the Conda environment, verify the
import path and style helper:

```cmd
python -c "import osdagbridge.core.reports.report_generator as r; print(r.__file__)"
python -c "from osdagbridge.core.reports.styles import apply_report_style; print('style import OK')"
```

Generate a report from the application. The output folder should contain the
PDF, the `.tex` source, an `assets` folder, and a compile log if compilation
fails. The assets folder is intentionally retained because the TeX source
uses relative paths to it.
