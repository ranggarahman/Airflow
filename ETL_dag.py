from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from twitter_extract import run_twitter_extract
from twitter_transform import run_twitter_transform
from twitter_load import run_twitter_load

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
    'ETL_dag',
    default_args=default_args,
    schedule_interval='0 */12 * * *',
    description='my etl code'
)

run_twitter_extract = PythonOperator(
    task_id='complete_twitter_extract',
    python_callable=run_twitter_extract,
    dag=dag,
)

run_twitter_transform = PythonOperator(
    task_id='complete_twitter_transform',
    python_callable=run_twitter_transform,
    dag=dag,
)

run_twitter_load = PythonOperator(
    task_id='complete_twitter_load',
    python_callable=run_twitter_load,
    dag=dag,
)

run_twitter_extract >> run_twitter_transform >> run_twitter_load
