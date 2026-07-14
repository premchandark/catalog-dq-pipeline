# remediation/remediate.py
# Applies safe automatic fixes and records an audit trail of every change made.

import pandas as pd

DEFAULT_CATEGORY = "Uncategorized"

def remediate(input_path="data/clean/catalog_classified.csv",
              output_path="data/clean/catalog_remediated.csv",
              audit_path="data/clean/remediation_audit.csv"):
    df = pd.read_csv(input_path)
    audit_records = []

    for idx, row in df.iterrows():
        if row["defect_type"] == "missing_category":
            audit_records.append({"product_id": row["product_id"], "field": "category",
                                   "original": None, "corrected": DEFAULT_CATEGORY})
            df.at[idx, "category"] = DEFAULT_CATEGORY

        elif row["defect_type"] == "negative_price":
            corrected_price = abs(row["price"])
            audit_records.append({"product_id": row["product_id"], "field": "price",
                                   "original": row["price"], "corrected": corrected_price})
            df.at[idx, "price"] = corrected_price

        # missing_title, missing_price, and broken_image_url are NOT auto-fixed —
        # they need human review. This is a deliberate design decision, not a gap:
        # you shouldn't invent a product title or a price automatically.

    audit_df = pd.DataFrame(audit_records)
    df.to_csv(output_path, index=False)
    audit_df.to_csv(audit_path, index=False)
    print(f"Auto-remediated {len(audit_df)} fields. {len(df[df['defect_type'].isin(['missing_title','missing_price','broken_image_url'])])} records still need manual review.")

if __name__ == "__main__":
    remediate()