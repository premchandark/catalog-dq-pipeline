# catalog_pipeline_dag.py
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="catalog_dq_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    generate = BashOperator(
        task_id="generate_catalog", 
        bash_command="cd /opt/project && python data_generator.py")
    validate = BashOperator(
        task_id="validate_quality", 
        bash_command="cd /opt/project && python data_quality/validate.py")
    classify = BashOperator(
        task_id="classify_defects", 
        bash_command="cd /opt/project && python defect_detection/classify.py")
    remediate = BashOperator(
        task_id="remediate", 
        bash_command="cd /opt/project && python remediation/remediate.py")
    model = BashOperator(
        task_id="dbt_run", 
        bash_command=(
            "cd /opt/project/dbt_project/catalog_dq && "
            "dbt run --profiles-dir /opt/project/dbt_project/catalog_dq && "
            "dbt test --profiles-dir /opt/project/dbt_project/catalog_dq"
        )
    )

    generate >> validate >> classify >> remediate >> model