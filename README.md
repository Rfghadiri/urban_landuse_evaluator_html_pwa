# Urban Land Use Evaluator

**A lightweight, browser-based tool for evaluating urban land-use provision against per-capita planning standards.**

Urban Land Use Evaluator is an early-stage web application designed to support urban planners, GIS specialists, and researchers in assessing land-use provision, identifying potential shortages and surpluses, and preparing preliminary evidence for planning decisions.

The project aims to make land-use standard evaluation more accessible through a simple Persian-friendly interface and a browser-based workflow.

## Key Features

- **Population-based evaluation:** Select the relevant population category for planning standards.
- **Data import:** Upload land-use data in CSV format.
- **Land-use mapping:** Match input land-use categories to standard categories.
- **Editable standards:** Adjust minimum and maximum per-capita thresholds.
- **Compliance assessment:** Identify potential shortages, surpluses, and cases within the specified standards.
- **Data quality checks:** Support preliminary review of unmatched or incomplete records.
- **Export results:** Download evaluation results in CSV format.
- **Preliminary SWOT analysis:** Organize evidence-based planning observations into strengths, weaknesses, opportunities, and threats.
- **TOWS strategy development:** Help translate SWOT findings into preliminary planning strategies.
- **Browser-based interface:** Run the application in a modern web browser.

## Project Status

**Early-stage prototype — active development**

The current version provides a preliminary workflow for land-use standards assessment. It is intended for exploratory analysis and decision support, not as a replacement for professional planning judgment or official statutory evaluation.

Some advanced planning rules, spreadsheet workflows, and spatial analysis functions are not yet implemented.

## Getting Started

### Option 1: Run the HTML File

1. Download or clone this repository.
2. Open `index.html` in a modern browser such as Google Chrome or Microsoft Edge.
3. Upload a CSV dataset and follow the on-screen instructions.

Some browser-based installation features may require running the application through a local server rather than opening the HTML file directly.

### Option 2: Run the Local Application

If the repository includes `start_windows.bat` and the associated local-server files:

1. Install Python if it is required by the provided launcher.
2. Extract the project files.
3. Run `start_windows.bat`.
4. Open the local address displayed in the terminal.
5. To install the app, use the browser's **Install app** option when available.

The local launcher and installation workflow depend on the files included in the downloaded release.

## Input Data

The current prototype supports CSV files containing land-use records.

Depending on the dataset, useful fields may include:

| Field | Description |
|---|---|
| Land-use category | The category assigned to each record |
| Area | The area associated with the land use |
| Population | Population used for per-capita calculations, where applicable |
| Identifier | A unique record or parcel identifier |

The actual column names can vary. Users should map their dataset fields to the relevant application inputs and verify units before interpreting results.

## Methodology

The general evaluation workflow consists of:

1. Importing land-use data.
2. Selecting the applicable population group and standards.
3. Mapping observed land-use categories to standard categories.
4. Defining or reviewing minimum and maximum per-capita thresholds.
5. Calculating preliminary compliance and identifying potential shortages or surpluses.
6. Reviewing data quality and unmatched categories.
7. Preparing preliminary SWOT findings and TOWS strategies based on the available evidence.

A calculated surplus does not automatically indicate a planning strength. Spatial distribution, accessibility, service capacity, population demand, and local context should also be considered.

Similarly, opportunities and threats generally require additional contextual evidence beyond numerical land-use calculations.

## Current Limitations

- CSV is the supported input and output format in the current prototype.
- Excel (`.xlsx`) import and export are not yet fully implemented in this HTML version.
- Advanced planning regulations and special-case rules require further implementation.
- GIS geometry, spatial accessibility, network analysis, and map-based evaluation are not currently implemented.
- SWOT and TOWS outputs should be reviewed by a qualified planning professional.
- Results depend on the quality of the input data and the validity of the selected standards.

## Roadmap

Planned development directions include:

- [ ] Excel import and export (`.xlsx`)
- [ ] Expanded Persian urban land-use standards
- [ ] Implementation of special regulations and planning footnotes
- [ ] More detailed data validation and reporting
- [ ] GIS integration and spatial accessibility analysis
- [ ] Evidence-linked SWOT and TOWS reporting
- [ ] Optional integration with local LLMs, including Ollama, for Persian-language planning analysis
- [ ] Improved offline support and cross-platform installation
- [ ] Automated report generation

## Intended Users

- Urban planners and land-use specialists
- GIS analysts
- Urban planning students and researchers
- Municipal planning departments
- Researchers working on urban standards and planning decision support

## Technology

The HTML edition is designed around browser-based technologies:

- HTML
- CSS
- JavaScript

Python may be required for the optional local-server launcher, depending on the release configuration.

## Contributing

Contributions, bug reports, and suggestions are welcome.

Potential areas for contribution include standards validation, Persian-language usability, data import/export, spatial analysis, and evidence-based planning reports.

Before submitting changes, please describe the issue, the proposed solution, and any relevant sample data or reproducible test case.

## Disclaimer

This tool is a research and decision-support prototype. Its outputs should not be treated as official planning approvals or definitive assessments of regulatory compliance without independent verification of the standards, calculations, data, and applicable regulations.

## License

No license has been specified yet. Until a license is added to the repository, reuse and redistribution permissions should not be assumed.

---

**Developed for urban planning, land-use evaluation, and data-informed planning research.**
