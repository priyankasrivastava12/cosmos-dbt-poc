from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from datetime import datetime

with DAG(
    dag_id="example_sql_execute_query_operator",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["snowflake", "sql"],
) as dag:

    run_query = SQLExecuteQueryOperator(
        task_id="run_sql_query",
        sql="SELECT CURRENT_DATE;",
        conn_id="snowflake_conn",  # This can be for Snowflake, Postgres, etc.
    )
