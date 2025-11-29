Guard Band Chart (GBC) Excel & Python Tool
1. Overview

This repository provides an Excel-based and Python-based tool for generating the Guard Band Chart (GBC) used in precision measurement and quality control.

The GBC visualizes:

- 1w, 2w, and 3w guard band boundaries

- Fully conforming / conditional / nonconforming zones

- Measurement trends for Part A, Part B, Part C

- Decision limits (TL, AL) based on measurement uncertainty

The tool is designed for general users, students, engineers, and researchers who want a simple and visual way to understand guard-band decision rules.



2. Files Included
/Excel_Tool/
   └─ GBC_Flatness_with_Charts.xlsx      → Excel file with auto-generated 1w/2w/3w GBC charts

/Python_Code/
   ├─ gbc_flatness_visualization.py      → Python script that generates GBC charts
   └─ requirements.txt                   → Required Python packages

/Screenshots/
   ├─ gbc_1w.png
   ├─ gbc_2w.png
   └─ gbc_3w.png

   

3. How to Use the Excel Tool
Excel Version (Easiest for General Users)

(1) Download GBC_Flatness_with_Charts.xlsx from the repository.

(2) Open the file in Excel.

(3) In the parameter table (right side of the sheet), you may adjust:

- TL (Tolerance Limit)

- uc (Standard uncertainty)

- k (Coverage factor)

(4) The following are automatically calculated:

- Guard band width w

- Acceptance limits AL (1w, 2w, 3w)

(5) The Excel file automatically updates three GBC charts:

- GBC (1w)

- GBC (2w)

- GBC (3w)

✔ No programming required
✔ Fully automated visualization
✔ Useful for training and industrial application



4. How to Use the Python Tool
Python Version (For flexible visualization or code modification)

(1) Install Python 3.x

(2) Install required packages:

pip install -r requirements.txt


(3) Run the visualization script:

python gbc_flatness_visualization.py


(4) This will generate three charts (1w/2w/3w) identical to the Excel version.

   

5. Example Visualizations (Screenshots)
1w Guard Band Chart

2w Guard Band Chart

3w Guard Band Chart

These images provide a clear view of how the GBC tool displays the tolerance limit (TL), acceptance limits (AL), and measurement data.



6. Key Concepts (Simple Explanation)

Below are essential concepts explained for general users:

(1) TL (Tolerance Limit)
The specification limit set by design or engineering standards.

(2) Uncertainty (uc)
A quantified estimate showing how much the measurement could vary.

(3) Guard Band Width (w = k·uc)
A safety margin applied to reduce false acceptance or false rejection.

(4) AL (Acceptance Limit)
The practical decision boundary used for quality inspection.

(5) Zones in GBC

- Fully Conforming Zone: Safe region

- Conditional Zone: Near borderline

- Nonconforming Zone: Fails the specification

  

7. Citation

If you use this tool in academic work, please cite:

Choi, I., and Hur, S. (2025). 
Design and Implementation of a Quality-Improvement-Oriented Guard Band Chart Based on Measurement Uncertainty.Hanyang University.



8. License

This project is freely available for academic, research, and educational purposes.
