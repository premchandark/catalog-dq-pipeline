# defect_detection/classify.py
# Classifies each product record with a defect_type based on simple, explainable rules.

import pandas as pd
import re

def classify_row(row):
    if pd.isna(row["title"]):
        return "missing_title"
    if pd.isna(row["category"]):
        return "missing_category"
    if pd.isna(row["price"]):
        return "missing_price"
    if row["price"] < 0:
        return "negative_price"
    if not re.match(r"^https?://", str(row["image_url"])):
        return "broken_image_url"
    return "clean"

def classify_catalog(input_path="data/raw/catalog_raw.csv", output_path="data/clean/catalog_classified.csv"):
    df = pd.read_csv(input_path)
    df["defect_type"] = df.apply(classify_row, axis=1)
    df.to_csv(output_path, index=False)
    print(df["defect_type"].value_counts())
    return df

if __name__ == "__main__":
    classify_catalog()