{{ config(materialized='table') }}
select
    vendor_id,
    category,
    defect_type,
    count(*) as defect_count
from {{ ref('stg_catalog') }}
where defect_type != 'clean'
group by 1, 2, 3