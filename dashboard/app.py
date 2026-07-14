# app.py
import streamlit as st
import duckdb
import pandas as pd

st.title("Catalog Data Quality Dashboard")

con = duckdb.connect("../catalog.duckdb")
summary = con.execute("SELECT * FROM defect_summary").fetchdf()
defects = con.execute("SELECT * FROM fact_catalog_defects").fetchdf()

st.subheader("Defect Rate by Category")
st.bar_chart(summary.set_index("category")["defect_rate_pct"])

st.subheader("Defect Breakdown")
st.dataframe(defects)

overall_rate = round(summary["defective_products"].sum() / summary["total_products"].sum() * 100, 2)
st.metric("Overall Catalog Defect Rate", f"{overall_rate}%")