# data_generator.py
# Generates a fake but realistic e-commerce product catalog with intentional data quality defects.

import pandas as pd
from faker import Faker
import random

fake = Faker()
random.seed(42)  # makes results repeatable

CATEGORIES = ["Electronics", "Home & Kitchen", "Sports", "Books", "Toys", "Beauty"]
VENDORS = [f"vendor_{i}" for i in range(1, 11)]  # 10 fake vendors

def generate_clean_product(product_id):
    return {
        "product_id": f"P{product_id:06d}",
        "title": fake.catch_phrase(),
        "category": random.choice(CATEGORIES),
        "price": round(random.uniform(5, 500), 2),
        "vendor_id": random.choice(VENDORS),
        "image_url": fake.image_url(),
        "created_at": fake.date_between(start_date="-1y", end_date="today"),
    }

def inject_defects(product, defect_rate=0.15):
    """Randomly corrupts a product record to simulate real-world messy vendor data."""
    if random.random() > defect_rate:
        return product, "clean"

    defect_type = random.choice([
        "missing_price", "negative_price", "missing_category",
        "duplicate_title_case", "broken_image_url", "missing_title"
    ])

    if defect_type == "missing_price":
        product["price"] = None
    elif defect_type == "negative_price":
        product["price"] = -abs(product["price"])
    elif defect_type == "missing_category":
        product["category"] = None
    elif defect_type == "duplicate_title_case":
        product["title"] = product["title"].upper()  # inconsistent formatting
    elif defect_type == "broken_image_url":
        product["image_url"] = "not_a_valid_url"
    elif defect_type == "missing_title":
        product["title"] = None

    return product, defect_type

def generate_catalog(n=1000):
    rows = []
    labels = []
    for i in range(n):
        product = generate_clean_product(i)
        product, label = inject_defects(product)
        rows.append(product)
        labels.append(label)
    df = pd.DataFrame(rows)
    df["_injected_defect_label"] = labels  # keep this for later accuracy scoring, drop before "production" use
    return df

if __name__ == "__main__":
    df = generate_catalog(1000)
    df.to_csv("data/raw/catalog_raw.csv", index=False)
    print(f"Generated {len(df)} products. Injected defect breakdown:")
    print(df["_injected_defect_label"].value_counts())