'''Update data in schema fgiski'''

'''Import libs'''
from airflow import DAG
from airflow.operators.python import PythonOperator

'''Import scripts for DAG'''
from dags.python_scripts import update_table_merchants

'''Import args for DAG'''
from python_scripts.config import dag_args


def foo():
    pass

with DAG('dag_name',
         description='dag_tag',
         schedule_interval='* * * * *',  # every minute
         catchup=False,
         default_args=dag_args
         ) as dag:
    update_table_merchants_task = PythonOperator(task_id='update_table_merchants',
                                                 python_callable=update_table_merchants.update)
    update_table_customers_task = PythonOperator(task_id='update_table_customers',
                                                 python_callable=update_table_customers.update)
    update_table_transactions_task = PythonOperator(task_id='update_table_transactions',
                                                 python_callable=update_table_transactions.update)
    '''DAG pipeline'''
    task_zero >> [update_table_merchants_task, update_table_customers_task] >> update_table_transactions_task
