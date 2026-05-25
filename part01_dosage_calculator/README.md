# Part 01: Clinical Drug Dosage Calculator 💊

## 📌 Project Overview
This is the first project of the Python for Bioentrepreneurship portfolio. It is a command-line tool designed to calculate medication dosages based on patient weight (mg/kg) and convert that dosage into an administrable liquid volume (mg/ml). 

## 🧬 Clinical & Strategic Value
In healthcare settings, dosage miscalculations are a critical safety risk. This script simulates a basic clinical safety workflow by:
1. Converting raw patient input into actionable clinical metrics.
2. Calculating required liquid volume for administration.
3. Implementing a hard safety threshold (`max_dosage`) to prevent accidental overdosing.

## 💻 Technical Concepts Applied
* **User Input & Variables:** Capturing terminal input (`input()`).
* **Type Casting:** Converting strings to floats for precise physiological calculations.
* **Conditionals:** Using `if/else` logic to evaluate clinical constraints.
* **Error Handling:** Implementing `try/except` blocks and raising `ValueError` to simulate system alerts.

## 🚀 How to Run
Navigate to this folder and execute the script in your terminal:
```bash
python main.py