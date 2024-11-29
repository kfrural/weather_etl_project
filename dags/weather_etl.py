from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_DIR = os.path.join(BASE_DIR, '../scripts')

def extract():
    exec(open(os.path.join(SCRIPTS_DIR, 'extract_weather.py')).read())

def transform():
    exec(open(os.path.join(SCRIPTS_DIR, 'transform_weather.py')).read())

def load():
    exec(open(os.path.join(SCRIPTS_DIR, 'load_weather.py')).read())

with DAG(
    dag_id='weather_etl',
    start_date=datetime(2024, 11, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:
    extract_task = PythonOperator(
        task_id='extract',
        python_callable=extract
    )
    transform_task = PythonOperator(
        task_id='transform',
        python_callable=transform
    )
    load_task = PythonOperator(
        task_id='load',
        python_callable=load
    )

    extract_task >> transform_task >> load_task
