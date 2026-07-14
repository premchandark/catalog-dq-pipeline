{{ config(materialized='table') }}
select
    category,
    count(*) as total_products,
    sum(case when defect_type != 'clean' then 1 else 0 end) as defective_products,
    round(100.0 * sum(case when defect_type != 'clean' then 1 else 0 end) / count(*), 2) as defect_rate_pct
from {{ ref('stg_catalog') }}
group by 1
order by defect_rate_pct desc