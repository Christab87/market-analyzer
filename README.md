# Financial Market Analyzer

![Financial Trend Analysis](assets/trend_plot.png)

A professional, modular Python data-analysis pipeline for financial time-series data. The project ingests CSV data, computes moving averages, and produces high-quality visualizations. It demonstrates software engineering best practices: separation of concerns, reproducible environments, automated test coverage, and synthetic data generation for testing.

## Project Structure

- `data/` - raw input CSV files (example: `raw_data.csv`)
- `assets/` - tracked images / documentation assets (e.g., `trend_plot.png`)  
- `output/` - runtime artifacts (generated charts) — ignored by Git
- `scripts/` - utility scripts (e.g., `generate_data.py`)
- `src/` - core application code
  - `analyzer.py` - data-processing logic
  - `visualizer.py` - plotting code
- `tests/` - pytest unit tests
- `main.py` - entry point
- `requirements.txt` - pinned dependencies
- `.python-version` (optional) - recommended Python version (e.g., `3.12`)
- `.gitignore` - ignore rules

## Prerequisites

- Python 3.12+ recommended
- Git
- pip

If you want to manage multiple Python versions locally, consider using `pyenv`. Place `3.12.x` as the project version to ensure compatibility with the pinned dependencies.

## Quickstart (recommended)

1. Clone the repository:
```bash
git clone https://github.com/yourusername/market_analyzer.git
cd market_analyzer
```

2. Create and activate a virtual environment:
```bash
# macOS / Linux
python -m venv venv
source venv/bin/activate

# Windows (PowerShell)
python -m venv venv
venv\Scripts\Activate.ps1
```

3. Install dependencies:
```bash
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
```

4. Generate synthetic test data:
```bash
python scripts/generate_data.py
```

5. Run the analysis and generate the visualization:
```bash
python main.py
```

6. View the result:
- A high-resolution plot `trend_plot.png` will be created in the `output/` folder.
- To show the image in the README, copy the desired image to `assets/trend_plot.png` and commit it.

## Usage Details

### Data format
Place your CSV in `data/raw_data.csv`. Required columns:
- `Date` — in `YYYY-MM-DD` format
- `Close` — numeric closing price

Example:
```csv
Date,Close
2024-01-01,150.00
2024-01-02,152.50
...
```

### Configuration
- Change moving-average window in `main.py`:
```python
analyzer.calculate_moving_average(window=7)
```
- Visualizer auto-detects any `SMA_<window>` column and plots it.

### Run as a module (alternative)
If you prefer running scripts as modules, ensure package folders have `__init__.py`. Example:
```bash
python -m scripts.generate_data
```
or run files directly:
```bash
python scripts/generate_data.py
```

## Testing

Run the test suite with:
```bash
pytest
```
Tests verify moving-average calculations and basic data validation. Add tests to `tests/` to cover new features.

## Development Notes

- Use `python -m pip` to ensure installation into the active virtual environment:
```bash
python -m pip install -r requirements.txt
```
- If you see Pandas warnings about `pyarrow`, install it (it is included in `requirements.txt`).

## Recommended Dependencies (see requirements.txt)
- pandas
- numpy
- pyarrow
- matplotlib
- pytest

All versions are pinned in `requirements.txt` for reproducibility.

## Git and Repo Hygiene

- `.gitignore` includes `venv/`, `output/`, `__pycache__/`, and editor settings.
- Keep generated runtime artifacts out of Git. Use `assets/` to store curated images for documentation.

Example `.gitignore` entries:
```text
venv/
output/
__pycache__/
.DS_Store
```

## License

Include a license file in the repo root (e.g., `LICENSE` with MIT License) to clarify usage terms.

