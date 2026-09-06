from datetime import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator


with DAG(
    dag_id="olist_end_to_end_pipeline",
    start_date=datetime(2026, 9, 1),
    schedule="@daily",
    catchup=False,
    tags=["olist", "clickhouse", "dbt", "data-engineering"],
) as dag:

    check_clickhouse = BashOperator(
    task_id="check_clickhouse",
    bash_command="""
python -c "
import os
import requests

host = os.getenv('CLICKHOUSE_HOST', 'clickhouse')
port = os.getenv('CLICKHOUSE_HTTP_PORT', '8123')

r = requests.get(
    f'http://{host}:{port}/ping',
    timeout=10
)

r.raise_for_status()
print('ClickHouse connection OK:', r.text.strip())
"
""",
)

    ingest_raw_data = BashOperator(
        task_id="ingest_raw_data",
        bash_command="""
python /opt/airflow/project/ingestion/load_to_clickhouse.py
""",
    )

    dbt_silver = BashOperator(
        task_id="dbt_silver",
        cwd="/opt/airflow/project/dbt/olist_transform",
        bash_command="""
dbt run --select path:models/silver
""",
    )

    dbt_gold = BashOperator(
        task_id="dbt_gold",
        cwd="/opt/airflow/project/dbt/olist_transform",
        bash_command="""
dbt run --select path:models/gold
""",
    )

    validate_data = BashOperator(
        task_id="validate_data",
        bash_command="""
python /opt/airflow/project/scripts/validate_data.py
""",
    )

    (
        check_clickhouse
        >> ingest_raw_data
        >> dbt_silver
        >> dbt_gold
        >> validate_data
    )
