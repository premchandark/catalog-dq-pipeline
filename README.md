Catalog Data Quality Platform
**Why I Built This**

Every data team depends on high-quality data.

Whether it's powering product recommendations, search results, pricing engines, or AI models, poor-quality data eventually becomes a business problem.

Missing product information, invalid categories, broken image URLs, or incorrect pricing don't just affect customers—they also reduce the reliability of analytics and machine learning systems.

I built this project to understand how modern data engineering teams improve data quality before it reaches downstream consumers.

Instead of treating data quality as a manual process, this platform automatically detects defects, classifies them, remediates deterministic issues, transforms the cleaned data, and exposes quality metrics through an analytics dashboard.

**Problem Statement**

Imagine an e-commerce marketplace where product data arrives from multiple vendors every day.

Because each vendor follows different standards, the catalog quickly becomes inconsistent.

Typical issues include:

Missing prices
Invalid categories
Broken image URLs
Incomplete product titles
Incorrect values

If these issues are not detected early, they propagate into search engines, recommendation systems, BI dashboards, and AI applications.

The challenge is building an automated pipeline that continuously validates, repairs, and monitors catalog quality without manual intervention.

**Project Goal**

The objective was to design a production-style data quality platform capable of:

✅ Simulating multi-vendor product data

✅ Detecting common quality issues

✅ Automatically remediating deterministic defects

✅ Tracking every remediation through audit logs

✅ Transforming cleaned datasets into analytics-ready models

✅ Providing stakeholders with real-time quality metrics

System Architecture

(Architecture diagram here)

Synthetic Catalog Generator
            │
            ▼
Validation Engine
            │
            ▼
Defect Classification
            │
            ▼
Auto Remediation
            │
            ▼
DuckDB
            │
            ▼
dbt Models
            │
            ▼
Streamlit Dashboard

Entire workflow orchestrated using Apache Airflow.

Engineering Decisions

This is the section recruiters actually read.

**Why Synthetic Data?**

Access to production catalog data is restricted.

Instead of relying on public datasets, I generated realistic vendor data using Faker while intentionally injecting quality defects to simulate production scenarios.

**Why Rule-Based Validation?**

Many data quality issues follow deterministic business rules.

Examples:

Price cannot be negative.
Category cannot be empty.
Image URL must follow a valid format.

A rule-based validator provides explainable and reliable quality checks before introducing more complex ML-based approaches.

**Why Auto Remediation?**

Not every defect requires human intervention.

Certain issues can be corrected automatically while preserving data lineage.

Examples:

Missing category → Default category
Negative price → Absolute value

This reduces manual effort while maintaining auditability.

**Why DuckDB?**

DuckDB provides analytical performance without requiring external infrastructure.

It allows local SQL analytics and integrates naturally with dbt for modeling.

**Why dbt?**

Raw validated data isn't optimized for reporting.

dbt transforms operational tables into analytics-ready models while documenting lineage and testing transformations.

**Why Airflow?**

Instead of manually executing scripts, the entire workflow is orchestrated through Airflow.

This enables:

Scheduling
Dependency management
Retry mechanisms
Pipeline monitoring
Key Features
Multi-vendor catalog simulation
Automated quality validation
Rule-based defect classification
Automatic remediation
Audit logging
dbt data modeling
Airflow orchestration
Interactive Streamlit dashboard
Modular pipeline design
Challenges I Solved
Building realistic test data

Random records aren't enough.

The challenge was generating synthetic data that closely resembles real e-commerce catalogs while injecting meaningful defects.

Designing reusable validation rules

Validation logic was modularized so new quality rules can be added without changing the overall pipeline.

Maintaining auditability

Every automatic correction is logged to preserve transparency and allow future debugging.

Keeping transformations reproducible

Using dbt ensures every transformation is version-controlled and reproducible.

Results

Pipeline successfully processed catalog data from:

10 Vendors
7 Product Categories

Generated:

Validation Reports
Defect Classification Reports
Remediation Audit Logs
Analytics Models
Interactive Dashboard

Overall catalog defect rate reduced to 12.1% after remediation.

**Future Improvements**

If this platform were deployed in production, I would extend it by adding:

Great Expectations for enterprise-grade validation
Kafka-based streaming ingestion
AWS S3 data lake integration
Glue Data Catalog
Athena analytics
Historical quality trend monitoring
CI/CD with GitHub Actions
ML-based anomaly detection
Slack/Email alerts for data quality failures
