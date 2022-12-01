from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

from datetime import datetime
from datetime import timedelta

from youtube_extract import run_youtube_extract
from youtube_transform import run_youtube_transform
from youtube_load import run_youtube_load

default_args = {
    'owner': 'airflow',
    'depends_on_past': 'false',
    'start_date': datetime(2022, 11, 29),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'ETL_dag_2',
    default_args=default_args,
    schedule_interval='0 */12 * * *',
    description='youtube etl'
)

run_youtube_extract = PythonOperator(
    task_id='complete_youtube_extract',
    python_callable=run_youtube_extract,
    dag=dag,
)

run_youtube_transform = PythonOperator(
    task_id='complete_youtube_transform',
    python_callable=run_youtube_transform,
    dag=dag,
)
run_youtube_load = PythonOperator(
    task_id='complete_youtube_load',
    python_callable=run_youtube_load,
    dag=dag,
)

run_youtube_extract >> run_youtube_transform >> run_youtube_load
