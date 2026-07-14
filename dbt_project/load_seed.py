import duckdb

con = duckdb.connect("../catalog.duckdb")  # dbt_project/ -> project root
con.execute("""
    CREATE OR REPLACE TABLE raw_catalog AS
    SELECT * FROM read_csv_auto('../data/clean/catalog_remediated.csv')
""")
print("Loaded raw_catalog table into DuckDB.")
con.close()