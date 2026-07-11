# Automated PDF-to-Excel Data Extraction & Cleaning Pipeline (ETL)

An end-to-end, automated Data Engineering solution designed to eliminate manual data entry. This Python-based ETL (Extract, Transform, Load) pipeline extracts unstructured data from PDF invoices, cleanses it by automatically removing duplicates and formatting errors, and outputs analytics-ready Excel spreadsheets.

## 🏗️ Data Architecture & Workflow
1. **Extract**: Reads text data page-by-page from raw PDF files using `pypdf`.
2. **Transform**: Cleans data using `Pandas`, removes duplicate rows, handles formatting, and maps data into structured tabular schemas.
3. **Load**: Automatically exports the clean, structured data into `.xlsx` format using `openpyxl`.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Core Libraries:** Pandas, PyPDF, OpenPyXL, ReportLab (for testing data generation)
* **Version Control:** Git & GitHub

## 📂 Project Structure
```text
automated-data-cleaning/
├── data/
│   ├── raw/          # Incoming raw PDF invoices/files (Ignored from version control)
│   └── processed/    # Generated clean Excel spreadsheets
├── src/
│   ├── create_pdf.py # Utility script to generate raw sample data
│   └── main.py       # Core ETL Pipeline script
├── .gitignore        # Ensures raw data privacy
└── README.md         # Documentation
```

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com
cd automated-pdf-to-excel-etl
```

### 2. Install dependencies
```bash
pip install pandas openpyxl pypdf reportlab
```

### 3. Generate sample data (Optional)
```bash
python src/create_pdf.py
```

### 4. Run the ETL Pipeline
```bash
python src/main.py
```
Check the `data/processed/` folder for your production-ready Excel file!
