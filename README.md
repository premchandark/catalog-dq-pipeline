# Catalog Data Quality Pipeline

An end-to-end data engineering pipeline that generates a realistic multi-vendor e-commerce product catalog, detects data quality issues, automatically remediates safe defects, transforms the data using dbt, orchestrates the workflow with Apache Airflow, and visualizes quality metrics through an interactive Streamlit dashboard.

---
## Project Overview

E-commerce platforms rely on high-quality catalog data for search, recommendations, pricing, and customer experience. However, product data often contains issues such as missing prices, invalid categories, broken image URLs, or incomplete product information.

This project simulates that real-world scenario by generating a synthetic product catalog, identifying data quality issues, applying rule-based validation, automatically fixing safe-to-remediate defects, and presenting the results through an analytics dashboard.

---
## Pipeline Architecture

```
Synthetic Catalog
        │
        ▼
Data Validation
        │
        ▼
Defect Classification
        │
        ▼
Auto Remediation
        │
        ▼
DuckDB + dbt
        │
        ▼
Streamlit Dashboard
```

Apache Airflow orchestrates the complete workflow.

---
## Features

- Generate realistic multi-vendor catalog data
- Detect common product catalog quality issues
- Classify defects by type and category
- Automatically remediate safe defects
- Maintain remediation audit logs
- Transform data using dbt
- Orchestrate pipeline using Airflow
- Interactive Streamlit dashboard

---
## Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Data Processing | Pandas, Faker |
| Data Warehouse | DuckDB |
| Data Modeling | dbt |
| Orchestration | Apache Airflow |
| Dashboard | Streamlit |
| Containerization | Docker |
| Version Control | Git, GitHub |

---
## Project Structure

```text
catalog-dq-pipeline/
│
├── data/
├── data_quality/
├── defect_detection/
├── remediation/
├── dbt_project/
├── orchestration/
├── dashboard/
├── docs/
├── data_generator.py
├── requirements.txt
└── README.md
```
---
## Workflow

### 1. Generate Catalog

Creates synthetic product catalog data using Faker with intentionally injected quality issues.

**Injected defects**

- Missing title
- Missing category
- Missing price
- Negative price
- Broken image URL

---
### 2. Validate Quality

Runs rule-based validation checks to identify invalid records.

---
### 3. Classify Defects

Groups detected issues into categories such as:

- missing_title
- missing_price
- missing_category
- negative_price
- broken_image_url

---
### 4. Auto Remediation

Automatically fixes deterministic issues.

| Defect | Action |
|---------|--------|
| Missing Category | Set to "Uncategorized" |
| Negative Price | Convert to positive value |

All changes are logged in an audit file.

---
### 5. Data Modeling

Loads cleaned data into DuckDB and creates analytics-ready models using dbt.

---
### 6. Dashboard

Visualizes:

- Defect rate by category
- Vendor-wise defect summary
- Overall catalog defect rate

---
## Dashboard

### Airflow Pipeline

![Airflow](docs/screenshots/airflow_dag_success.png)

---
### Defect Rate by Category

![Dashboard](docs/screenshots/streamlit_dashboard_chart.png)

---
### Defect Breakdown

![Breakdown](docs/screenshots/streamlit_defect_breakdown.png)

---
## Pipeline Metrics

| Metric | Value |
|---------|------:|
| Vendors | 10 |
| Categories | 7 |
| Overall Defect Rate | 12.1% |
| Airflow Tasks | 5 |
| Pipeline Status | Successful |
| Runtime | 2 min 42 sec |

---
## Run Locally

Clone the repository

```bash
git clone https://github.com/<username>/catalog-dq-pipeline.git
cd catalog-dq-pipeline
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run manually

```bash
python data_generator.py
python data_quality/validate.py
python defect_detection/classify.py
python remediation/remediate.py

cd dbt_project
python load_seed.py

cd catalog_dq
dbt run --profiles-dir .
dbt test --profiles-dir .
```

Start dashboard

```bash
cd dashboard
streamlit run app.py
```

Run through Airflow

```bash
cd orchestration
docker compose up -d
```

Open:

- Airflow → `http://localhost:8080`
- Dashboard → `http://localhost:8501`

---
## Future Improvements

- Kafka streaming ingestion
- Great Expectations integration
- CI/CD with GitHub Actions
- Cloud deployment (AWS)
- Historical quality monitoring
- ML-based anomaly detection

---
