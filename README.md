# 🏙️ Urban Land Use Evaluator (ULE)

### Version 2.0 — AI Agent, Python (Pyodide), and CA–Markov Forecasting

An integrated computational platform for urban land-use evaluation, spatial analysis, accessibility assessment, land-use change forecasting, and AI-assisted urban planning.

---

## Overview

**Urban Land Use Evaluator (ULE)** is a web-based analytical application designed to support urban planners, GIS specialists, researchers, and spatial data analysts in evaluating urban land-use patterns and assessing the spatial distribution of urban services.

Version **2.0** introduces a new generation of analytical capabilities, combining conventional land-use evaluation with an interactive **AI Agent**, an in-browser **Python execution environment powered by Pyodide**, and **CA–Markov land-use change forecasting**.

The application integrates GIS-based analysis, quantitative planning standards, Python programming, and artificial intelligence within a unified urban-planning environment.

## What's New in Version 2.0

### 1. AI Agent for Urban Planning

ULE 2.0 introduces an interactive AI Agent designed to assist users in analyzing project data and modifying application parameters through natural-language commands.

Key capabilities:

- Interactive AI-powered assistance.
- Analytical interpretation of project data.
- Context-aware responses based on the active project.
- Natural-language modification of project parameters.
- Direct updates to application tables and forms.
- Support for changing population, land-use areas, planning standards, and forecasting parameters.
- Assistance with urban-planning analysis and interpretation.

The AI Agent communicates with a lightweight **FastAPI backend**, which connects the application to an AI model provider.

### 2. Python Coding Environment — Pyodide

ULE 2.0 includes an integrated Python execution environment powered by **Pyodide**, allowing users to write and execute Python code directly in the browser.

Key capabilities:

- In-browser Python execution.
- Custom analytical scripting.
- Support for compatible Python libraries, including `pandas`.
- Access to analytical workflows without requiring a local Python installation for browser-based execution.
- A flexible environment for extending the application's analytical capabilities.

The Python environment provides a foundation for developing custom urban-planning methods and conducting additional quantitative analyses.

### 3. CA–Markov Land-Use Change Forecasting

Version 2.0 introduces a spatially explicit land-use change forecasting module based on the integration of **Markov transition modeling** and **Cellular Automata (CA)**.

The forecasting framework combines:

- Markov transition probabilities for estimating quantitative land-use demand.
- Cellular Automata for spatial allocation of projected land-use changes.
- Moore neighborhood configuration using a `3 × 3` neighborhood.
- Spatial simulation of land-use transitions.
- User-defined forecasting parameters and target years.

The model supports the simulation of future land-use patterns by integrating temporal transition probabilities with neighborhood-based spatial interactions.

### 4. GIS-Based Spatial and Strategic Analysis

ULE 2.0 provides analytical tools for evaluating the spatial distribution and accessibility of urban services.

Key capabilities:

- Buffer-based service-area analysis.
- Road-network accessibility analysis.
- Shapefile-based road-network processing.
- Spatial evaluation of urban facilities.
- Interactive SVG charts and visualizations.
- Automated preliminary SWOT/TOWS analysis.

---

## Core Features

### Urban Land-Use Evaluation

- Import and process urban land-use datasets.
- Calculate land-use areas and per-capita indicators.
- Evaluate the distribution of urban land uses.
- Assess land-use composition and spatial patterns.
- Support quantitative evaluation of urban service provision.

### Population Standards Assessment

ULE supports per-capita evaluation based on approved population-based planning standards.

The application includes support for the population-group standards specified in **Table 3 of the relevant Supreme Council of Urban Planning and Architecture resolution**.

Key capabilities:

- Calculate land-use per-capita values.
- Compare existing per-capita values with planning standards.
- Identify land-use shortages and surpluses.
- Estimate required land-use areas based on population.
- Support quantitative assessment of urban service provision.

### Data Import

The application supports the following input formats:

**Shapefile**
- `.shp` — Geometry
- `.dbf` — Attribute data
- `.prj` — Coordinate reference system
- `.cpg` — Character encoding, when available

**CSV**
- Tabular data for land-use evaluation and related analytical workflows.

Users should ensure that spatial datasets use an appropriate coordinate reference system and that attribute fields are correctly structured.

### Accessibility Analysis

- Buffer-based service-area analysis.
- Evaluation of service coverage.
- Assessment of the spatial distribution of urban facilities.
- Identification of areas with insufficient access to services.

### Road Network Analysis

- Import road-network shapefiles.
- Analyze accessibility through the street network.
- Evaluate the spatial relationship between urban services and transportation infrastructure.
- Support network-based service accessibility assessment.

### Land-Use Change Forecasting

- Markov transition probability modeling.
- Cellular Automata-based spatial allocation.
- Moore neighborhood configuration (`3 × 3`).
- Simulation of future land-use patterns.
- Analysis of projected land-use transitions.

### Analytical Visualization

- Interactive SVG charts.
- Statistical summaries.
- Land-use distribution visualization.
- Spatial and quantitative analytical outputs.

### SWOT/TOWS Analysis

- Automated preliminary SWOT analysis.
- Identification of strengths, weaknesses, opportunities, and threats.
- Support for strategic interpretation of urban-planning results.
- Preliminary TOWS-based strategic recommendations.

AI-generated SWOT/TOWS outputs should be reviewed and validated by the user before being used in formal planning documents.

---

## Technology Stack

| Component | Technology |
|---|---|
| User Interface | HTML5 |
| Styling | CSS3 |
| Application Logic | JavaScript |
| Python Runtime | Pyodide |
| Python Data Analysis | pandas |
| AI Backend | FastAPI |
| Backend Server | Uvicorn |
| AI Provider | Groq API |
| Forecasting Method | CA–Markov |
| Spatial Data | ESRI Shapefile, CSV |
| Visualization | SVG-based interactive charts |

---

## Installation and Setup

The main application runs in a web browser. The AI Agent requires a separate local FastAPI backend.

### 1. Requirements

- Python 3.9 or later.
- A modern web browser, such as Google Chrome or Microsoft Edge.
- A Groq API key.
- Internet access for the AI API and any externally loaded application resources.

Obtain an API key from:

[Groq Console](https://console.groq.com/)

### 2. Download the Backend

Download `main.py` from your repository or clone the project.

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

If you only need the backend, download `main.py` and place it in a dedicated directory, such as:

```text
F:\Server
```

### 3. Install Backend Dependencies

Open Command Prompt or PowerShell and run:

```bash
python -m pip install fastapi uvicorn httpx
```

### 4. Configure the Groq API Key

For security, do not publish your API key directly in `main.py` or commit it to GitHub.

Set the API key as an environment variable.

**Windows PowerShell:**

```powershell
$env:GROQ_API_KEY="YOUR_GROQ_API_KEY"
```

**Windows Command Prompt:**

```cmd
set GROQ_API_KEY=YOUR_GROQ_API_KEY
```

The backend should read the key from the environment:

```python
import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
```

If the key is not configured, the backend should report a configuration error rather than attempting an authenticated request.

### 5. Run the Backend

Navigate to the directory containing `main.py`.

For example:

```powershell
F:
cd Server
```

Start the FastAPI server:

```bash
python -m uvicorn main:app --reload --port 8000
```

When the server starts successfully, the terminal should display a message similar to:

```text
INFO: Uvicorn running on http://127.0.0.1:8000
INFO: Application startup complete.
```

Keep the terminal window open while using the AI Agent.

The backend is now available at:

`http://127.0.0.1:8000`

---

## Connecting the AI Agent

### 1. Open the Application

Open `index.html` in Google Chrome or Microsoft Edge.

### 2. Open the AI Assistant

Click the floating **AI Assistant** button located in the application interface.

### 3. Configure the Backend Address

Enter the local backend address:

```text
http://127.0.0.1:8000
```

### 4. Load Available Models

Click **Get Models** to retrieve available models from the configured AI provider.

Select a supported model, such as:

```text
llama-3.3-70b-versatile
```

The available models depend on the provider's current API availability and account access.

### 5. Start Using the AI Agent

You can now enter natural-language commands to analyze project data or modify supported application parameters.

---

## Example AI Agent Commands

The AI Agent supports natural-language interaction with project data.

Examples:

**Population**

```text
Change the base population to 1,961,260.
```

**Land-use area**

```text
Increase the park land-use area to 250,000 square meters.
```

**Planning standards**

```text
Set the minimum standard for park land use to 10 square meters per capita.
```

**Project information**

```text
Change the project name to Isfahan Master Plan.
```

**Analytical interpretation**

```text
Analyze the current per-capita land-use shortages and provide planning recommendations.
```

**Forecasting parameters**

```text
Change the target year of the CA–Markov forecast.
```

The AI Agent uses the active project context to generate responses and structured actions. Supported actions can update application tables and forms directly.

---

## Python Coding Environment

The integrated Python environment allows users to execute Python code directly in the browser through Pyodide.

Example:

```python
import pandas as pd

data = {
    "land_use": ["Residential", "Park", "Educational"],
    "area_m2": [1500000, 250000, 180000]
}

df = pd.DataFrame(data)

df["share_percent"] = (
    df["area_m2"] / df["area_m2"].sum() * 100
)

print(df)
```

The Python environment can be used for custom calculations, data manipulation, and analytical experimentation.

Package availability depends on Pyodide compatibility and the packages supported by the configured runtime.

---

## CA–Markov Forecasting Workflow

The land-use forecasting module follows a general workflow:

1. Prepare historical land-use data.
2. Define the base year and forecasting target year.
3. Estimate land-use transition probabilities using Markov modeling.
4. Calculate projected land-use demand.
5. Apply Cellular Automata for spatial allocation.
6. Evaluate neighborhood influence using the Moore neighborhood.
7. Generate the simulated future land-use map.
8. Analyze projected land-use changes.

The forecasting results should be interpreted as model-based simulations rather than deterministic predictions of future urban development.

---

## Project Structure

A typical project structure may look like:

```text
Urban-Land-Use-Evaluator/
│
├── index.html
├── main.py
├── README.md
│
└── data/
    ├── landuse.shp
    ├── landuse.dbf
    ├── landuse.prj
    └── landuse.cpg
```

The exact structure may vary depending on the project configuration and the datasets used.

---

## Security and Usage Notes

- Keep API keys private.
- Do not commit credentials to public repositories.
- Configure backend access and CORS policies appropriately.
- Do not expose the AI backend to public networks without suitable authentication and security controls.
- Review AI-generated analytical interpretations before using them in formal planning documents.
- Validate input data, coordinate systems, and forecasting assumptions before interpreting results.

---

## Intended Users

- Urban Planners
- GIS Specialists
- Urban Researchers
- Spatial Data Analysts
- Planning Consultants
- University Students

---

## Development Direction

ULE 2.0 establishes a foundation for further development in:

- Advanced CA–Markov forecasting.
- Machine-learning-based urban analysis.
- GeoAI and spatial modeling.
- Automated Word report generation.
- Advanced Python-based geospatial processing.
- AI-assisted urban planning workflows.
- Integration of custom analytical models.

---

## Project Objective

The long-term objective of Urban Land Use Evaluator is to develop an extensible computational environment that integrates:

**GIS + Python + Artificial Intelligence + Urban Planning**

within a unified platform for quantitative urban analysis, spatial evaluation, and evidence-based planning.

---

**Urban Land Use Evaluator — Version 2.0**

*Bridging GIS, Python, Artificial Intelligence, and Urban Planning.*
