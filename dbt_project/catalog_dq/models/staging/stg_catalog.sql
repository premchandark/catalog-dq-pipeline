-- stg_catalog.sql: cleaned, typed, one row per product
select
    product_id,
    trim(title) as title,
    category,
    cast(price as decimal(10,2)) as price,
    vendor_id,
    defect_type,
    created_at
from raw_catalog