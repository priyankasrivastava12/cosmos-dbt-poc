from datetime import datetime
import os
from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import PostgresUserPasswordProfileMapping
from cosmos.profiles import SnowflakeUserPasswordProfileMapping


profile_config = ProfileConfig(profile_name="dbtlearn",
                               target_name="dev",
                               profile_mapping=SnowflakeUserPasswordProfileMapping(conn_id="snowflake_conn", 
                                                    profile_args={
                                                        "database": "AIRBNB",
                                                        "schema": "DEV"
                                                        },
                                                    ))


dbt_snowflake_dag = DbtDag(project_config=ProjectConfig("/usr/local/airflow/dags/dbt/dbtlearn",),
                    operator_args={"install_deps": True},
                    profile_config=profile_config,
                    execution_config=ExecutionConfig(dbt_executable_path=f"{os.environ['AIRFLOW_HOME']}/dbt_venv/bin/dbt",),
                    schedule="@daily",
                    start_date=datetime(2023, 9, 10),
                    catchup=False,
                    dag_id="dbt_snowflake_dag",)