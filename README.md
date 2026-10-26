# URBAN LAND-USE EVALUATOR
## Complete English User Guide

**Application:** Offline HTML prototype  
**Purpose:** Preliminary per-capita land-use evaluation and geometric service-buffer analysis

---

## 1. Overview

This prototype supports preliminary evaluation of urban land-use provision per capita using a reference population and the standard ranges embedded in the application. It also provides data-quality checks, mapping of input land-use labels to standard categories, an initial SWOT/TOWS assessment, and geometric visualization of service locations and circular buffers.

> **Important:** This is a prototype for analysis and workflow testing. It does not replace professional review, approved planning regulations, or legal verification of standards.

## 2. Run the Application

1. **Extract** the ZIP archive to a folder.
2. **Open** `index.html` in an up-to-date browser, such as Google Chrome, Microsoft Edge, or Firefox.
3. **Work offline:** normal use does not require Python or an internet connection.
4. When exporting results, check your browser's download location and save prompt.

---

## 3. Per-Capita Land-Use Evaluation

### Workflow

1. Enter the **project name** and the **planning-baseline population**.
2. Upload a land-use **CSV file**, or use the sample-data option.
3. Select the columns for **land use** and **area**, plus an identifier column if available.
4. In the land-use mapping section, map each input label to its corresponding standard category.
5. Run the calculation or report-update action.
6. Review the results, active standards, data-quality checks, and preliminary SWOT/TOWS assessment. Export results as needed.

### Recommended CSV format

```csv
parcel_id,land_use,area_m2
P001,Educational,40000
P002,Park,80000
```

### Data requirements and notes

- **File format:** CSV is recommended; use UTF-8 encoding.
- **Area:** `area_m2` must contain numeric values in square metres.
- **Population:** The population entered in the application is the denominator for per-capita calculations of aggregated land-use categories.
- **Standards:** You can edit standard ranges for the current analysis. These edits do not change the embedded reference file.
- **Commercial/service adjustment:** Enable the **0.5 m² adjustment** only when the condition specified in the relevant standards note applies.

---

## 4. Service Locations and Buffer Analysis

### Workflow

1. Open the **Service Spatial Analysis** tab.
2. Upload a CSV of service locations, or select the sample-points option.
3. Check the columns assigned to **service type**, **X**, **Y**, and **identifier**.
4. Enter the project's **UTM zone** in the project information.
5. In the standard-radius table, enter a **buffer radius in metres** for each service type.
6. Review the geometric map, analytical diagram, and summary indicators.
7. Export the required outputs, if needed.

### Recommended CSV format

```csv
id,land_use,x,y
S001,School,537000,3628000
S002,Park,537400,3627600
```

### Coordinate requirements

- **X = Easting** and **Y = Northing**.
- Coordinates must be in **metres** and use the same projected coordinate reference system, UTM zone, and hemisphere.
- Sample coordinates are synthetic and must **not** be used for real-world analysis.
- The output is a geometric map of points and circular buffers; it is **not** a street basemap or a GIS background map.
- Buffer radii must be supplied by the user based on an applicable, reliable standard for each service type. Default values, if present, should not be treated as legally authoritative.

### Interpreting buffer results

- Circular buffers represent **straight-line (Euclidean) distance**, not travel distance or travel time along the street network.
- A point falling within another service's buffer does not indicate how many residents are served.
- Estimating population coverage requires spatial population data, such as census blocks or a population grid.

---

## 5. Available Exports

| Output | Format |
|---|---|
| Per-capita evaluation results | CSV |
| Evaluation summary | CSV |
| SWOT/TOWS report | TXT |
| Land-use data template | CSV |
| Service-location data template | CSV |
| Geometric buffer map | SVG or PNG |
| Service analytical diagram | SVG |
| Summary by service type, including point counts and entered radii | CSV |

**Note:** The application does not currently import or export XLSX files directly. Use CSV files instead.

---

## 6. Standards Reference and Limitations

- Some special provisions and domain-specific rules—including rules that depend on student population and special cemetery calculations—may not be calculated automatically and may require expert interpretation.
- Per-capita provision alone does not establish the adequacy or spatial equity of service access.
- The embedded standards reference identifies **Table 3 of the resolution dated 10 June 2010** (20 Khordad 1389 in the Iranian calendar) of Iran's Supreme Council of Urban Planning and Architecture.
- The current validity and legal status of the referenced standards must be **verified independently** before formal or regulatory use.

---

## 7. Troubleshooting

| Issue | What to check |
|---|---|
| Columns are detected incorrectly | Select the correct columns manually from the dropdown lists. |
| The map does not appear | Confirm that X and Y contain numeric values and use a consistent projected coordinate system. |
| A buffer is not visible | Enter a radius greater than zero for the relevant service type. |
| Persian text appears garbled in a CSV | Save or re-export the file using UTF-8 encoding. |
| An exported file is difficult to find | Check your browser's default Downloads folder and any save dialog. |

---

## Before Using Results in an Official Report

**Independently verify the calculations, the applicable standards, and the interpretation of every output.** Treat results as preliminary until they have been reviewed by a qualified planning professional.
