import os
from datetime import datetime
from dotenv import load_dotenv

from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping

load_dotenv()

ELT_PROJECT_DIR = os.getenv('ELT_PROJECT_DIR')

# Define the profile configuration
profile_config = ProfileConfig(
    profile_name="default",
    target_name="dev",
    profile_mapping=SnowflakeUserPasswordProfileMapping(
        conn_id="snowflake_conn",
        profile_args={"database": "dbt_db", "schema": "dbt_schema"},
    ),
)

# Define dbt snowflake dag
dbt_snowflake_dag = DbtDag(
    project_config=ProjectConfig(ELT_PROJECT_DIR),
    operator_args={"install_deps": True},
    profile_config=profile_config,
    execution_config=ExecutionConfig(dbt_executable_path=f"{os.environ['AIRFLOW_HOME']}/dbt_venv/bin/dbt",),
    schedule_interval="@daily",
    start_date=datetime(2023, 9, 10),
    catchup=False,
    dag_id="dbt_dag",
)