# data_quality/validate.py (fallback, no external DQ library dependency)
import pandas as pd
import re

def validate_catalog(input_path="data/raw/catalog_raw.csv"):
    df = pd.read_csv(input_path)
    checks = {
        "product_id_not_null": df["product_id"].notna().all(),
        "title_not_null": df["title"].notna().all(),
        "category_not_null": df["category"].notna().all(),
        "price_in_range": df["price"].dropna().between(0.01, 100000).all(),
        "image_url_valid_format": df["image_url"].dropna().apply(lambda x: bool(re.match(r"^https?://", str(x)))).all(),
    }
    success = all(checks.values())
    failed = [name for name, passed in checks.items() if not passed]
    print(f"Validation success: {success}")
    print(f"Total checks run: {len(checks)}")
    print(f"Failed checks: {failed}")
    return checks

if __name__ == "__main__":
    validate_catalog()