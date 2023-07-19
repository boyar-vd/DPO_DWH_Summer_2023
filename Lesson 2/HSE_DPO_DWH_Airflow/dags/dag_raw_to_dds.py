'''Update data in schema fgiski'''

'''Import libs'''
from airflow import DAG
from airflow.operators.python import PythonOperator

'''Import scripts for DAG'''
from dags.python_scripts import update_table_merchants

'''Import args for DAG'''
from python_scripts.config import dag_args

with DAG('dag_name',
         description='dag_tag',
         schedule_interval='* * * * *',  # every minute
         catchup=False,
         default_args=dag_args
         ) as dag:
    update_table_merchants_task = PythonOperator(task_id='update_table_merchants',
                                                 python_callable=update_table_merchants.update())
    '''DAG pipeline'''
    update_table_merchants_task
