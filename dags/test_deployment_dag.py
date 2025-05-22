from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello_astronomer():
    print("✅ Hello from Astronomer! Deployment successful.")

with DAG(
    dag_id="test_deployment_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,  # Manual trigger only
    catchup=False,
    tags=["test"],
) as dag:

    hello_task = PythonOperator(
        task_id="say_hello",
        python_callable=hello_astronomer,
    )
