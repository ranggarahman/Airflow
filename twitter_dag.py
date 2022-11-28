from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from twitter_etl import run_twitter_extract

default_args = {
    'owner': 'airflow',
    'depends_on_past': 'false',
    'start_date': datetime(2022, 11, 11),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'twitter_dag',
    default_args=default_args,
    description='my etl code'
)

run_twitter_extract = PythonOperator(
    task_id='complete_twitter_extract',
    python_callable=run_twitter_extract,
    dag=dag,
)

run_twitter_extract