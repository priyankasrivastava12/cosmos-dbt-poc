import os
import logging
from datetime import datetime, timedelta

from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping

logger = logging.getLogger("airflow.task")

# Define the dbt profile connection
profile_config = ProfileConfig(
    profile_name="dbtlearn",
    target_name="dev",
    profile_mapping=SnowflakeUserPasswordProfileMapping(
        conn_id="snowflake_conn",  # ✅ Must be defined in Astronomer Cloud Airflow UI
        profile_args={
            "database": "AIRBNB",
            "schema": "DEV"
        },
    ),
)

# Define the DAG
dbt_dag = DbtDag(
    dag_id="dbt_test_dag",
    project_config=ProjectConfig("/usr/local/airflow/dags/dbt/dbtlearn"),
    profile_config=profile_config,
    operator_args={"install_deps": True},
    execution_config=ExecutionConfig(
        dbt_executable_path=f"{os.environ.get('AIRFLOW_HOME')}/dbt_venv/bin/dbt",
        dbt_args={"select": "fct_listings_and_reviews"}  # ✅ Replace with any valid model name
    ),
    schedule=None,  # Manual trigger
    start_date=datetime.now() - timedelta(days=1),
    catchup=False,
)

# Log confirmation
logger.info("✅ DAG 'dbt_test_dag' has been set up with Cosmos and dbt")
