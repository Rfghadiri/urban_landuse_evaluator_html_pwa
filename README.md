# Urban Land Use Evaluator & Spatial Network Analysis

A GIS-based application for evaluating urban land-use distribution, calculating service-area standards, and performing spatial accessibility analysis through road networks.

The application is designed to support urban planners, GIS analysts, and urban development researchers in assessing existing land-use patterns and identifying spatial deficiencies in urban services.

---

## Key Features

### 1. Urban Land-Use Evaluation
- Import urban land-use data directly from **ESRI Shapefile**.
- Read polygon geometries and attribute tables.
- Select land-use classification fields from the shapefile attribute table.
- Calculate land-use areas automatically from polygon geometries.
- Calculate existing per-capita land-use standards.
- Compare existing per-capita values with predefined planning standards.
- Identify land-use deficiencies and surpluses.
- Generate statistical summaries and comparative charts.

### 2. Service Area Buffer Analysis
- Import service locations using CSV files.
- Define service buffer distances.
- Analyze the spatial coverage of urban facilities.
- Evaluate service accessibility using Euclidean buffer distances.
- Visualize service coverage and spatial distribution.

### 3. Road Network Analysis
- Import road network data from ESRI Shapefile (`.shp`).
- Import service locations independently using CSV files.
- Build a graph-based road network from line geometries.
- Connect service locations to the nearest road network edges.
- Perform network-distance accessibility analysis using shortest-path algorithms.
- Identify accessible and inaccessible network areas within specified distance thresholds.
- Export analytical results as CSV files.

### 4. Reporting and Visualization
- Generate statistical summaries of land-use distribution.
- Visualize land-use composition and service accessibility.
- Compare existing land-use standards against planning benchmarks.
- Export analytical data for further GIS processing.

---

## Input Data Requirements

### Land-Use Shapefile

Required files:

- `.shp` — Polygon geometries
- `.dbf` — Attribute table
- `.shx` — Shape index
- `.prj` — Coordinate reference system (strongly recommended)

The shapefile should contain a field representing land-use categories.

**Important — Character Encoding Limitation**

The application currently has limitations when reading Persian characters from shapefile attribute tables.

For reliable results, it is strongly recommended to:

- Use **English characters** for land-use categories and attribute values.
- Use English field names in the DBF attribute table.
- If Persian attributes are required, save the DBF text encoding as **Windows-1256**.
- Include a `.cpg` file specifying the encoding when available.

Example:

| landuse_code | landuse_name |
|---|---|
| 1 | Residential |
| 2 | Commercial |
| 3 | Educational |
| 4 | Medical |
| 5 | Green Space |
| 6 | Administrative |

Using English attribute values is the preferred approach for maximum compatibility.

### Service Locations CSV

The CSV file should contain at least two coordinate fields:

| id | service_type | name | X | Y |
|---|---|---|---:|---:|
| S001 | Hospital | Hospital 1 | 510250 | 3622500 |
| S002 | School | School 1 | 512100 | 3623900 |
| S003 | Park | Park 1 | 511300 | 3621700 |

The coordinate fields must use a projected coordinate reference system with metric units.

---

## Coordinate Reference System (CRS)

For accurate area and network-distance calculations:

- Use a projected coordinate system.
- Coordinates must be expressed in meters.
- Ensure that land-use polygons, road networks, and service locations share the same CRS.

For Isfahan, Iran, **WGS 84 / UTM Zone 39N (EPSG:32639)** can be used where appropriate.

> Geographic coordinates (latitude/longitude) should not be used directly for planar area or metric network-distance calculations.

---

## Technical Overview

| Component | Description |
|---|---|
| Platform | Web-based application |
| Interface | HTML, CSS, JavaScript |
| GIS Data | ESRI Shapefile |
| Tabular Data | CSV |
| Spatial Analysis | Polygon area and buffer analysis |
| Network Analysis | Graph construction and shortest-path analysis |
| Visualization | Interactive charts and spatial representations |
| Output | CSV and analytical summaries |

---

## Limitations

- Shapefile attribute encoding may affect the correct display of Persian text. Windows-1256 is recommended for Persian DBF attributes; English attribute values are preferred.
- Network analysis performance depends on the number of road segments and available browser memory.
- Accurate network analysis requires valid road geometries and appropriate network connectivity.
- Service locations must be in the same projected CRS as the road network.
- The application does not automatically correct topological errors or reproject all input datasets.
- Online basemaps, where used, require an internet connection.

---

## Getting Started

1. Download the latest ZIP release.
2. Extract the application files.
3. Open the HTML file in a modern web browser.
4. Import your land-use shapefile or service-location CSV.
5. Configure the required analytical parameters.
6. Run the desired spatial analysis.
7. Review the results and export the analytical data.

No server-side installation is required for the basic application workflow.

---

## Intended Applications

- Urban land-use assessment
- Per-capita urban service evaluation
- Urban facility accessibility analysis
- Road-network-based service accessibility
- Identification of spatial service deficiencies
- Urban planning and development studies
- GIS-based decision support

---

## Future Development

Potential improvements include:

- Native Persian RTL Word report generation (`.docx`).
- Improved automatic character-encoding detection.
- GeoPackage support.
- Advanced network topology validation.
- Large-scale network processing.
- Additional accessibility and spatial equity indicators.
- Integration with Python-based geospatial processing.

---

## License

## License

Copyright © 2026 Aref Ghadiri. All rights reserved.

This project is developed for academic and research purposes in the field of urban planning and geospatial analysis, with an academic affiliation to **Art University of Isfahan, Iran**.

No permission is granted to redistribute, modify, or commercially use this software without prior written permission from the copyright holder, except where otherwise explicitly authorized.

Any authorized redistribution, modification, or academic use must retain the original copyright notice and include clear attribution to the original GitHub repository:

**Original Repository:**  
https://github.com/Rfghadiri/urban_landuse_evaluator_html_pwa

**Academic Affiliation:**  
Art University of Isfahan, Iran.

## Attribution and Citation

If you use, reference, adapt, or incorporate this software into academic research, publications, reports, or derivative projects, please acknowledge the original work.

**Recommended citation:**

Ghadiri, A. (2026). *Urban Land Use Evaluator & Spatial Network Analysis* [Software]. GitHub. https://github.com/Rfghadiri/urban_landuse_evaluator_html_pwa

**Academic affiliation:** Art University of Isfahan, Isfahan, Iran.

Please retain the original repository URL in any derivative or redistributed version. The mention of Art University of Isfahan indicates academic affiliation and does not imply official university endorsement or ownership.


---

**Developed for GIS-based urban planning, land-use evaluation, and spatial accessibility analysis.**
