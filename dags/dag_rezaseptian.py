import pendulum
import pandas as pd
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.models import Variable
from sqlalchemy import create_engine
from airflow.operators.bash import BashOperator

import files.func_python as func

# Ambil environment dari Variable
env = Variable.get('my_credential', deserialize_json=True)
db_uri = env['db_neon']
conn_target = 'postgre_conn' 
path_file = 'dags/files/telecom_users.csv'

# Task BashOperator untuk cek koneksi database
check_db_connection_task = BashOperator(
    task_id='check_database_connection',
    bash_command='echo "Memeriksa koneksi database..." && '
                 'psql "${DB_URI}" -c "SELECT 1 AS connection_test"',
        env={'DB_URI': db_uri},  
    )

# Fungsi untuk insert data dari CSV ke Postgres
def insert_data(file_path, db_target):
    engine = create_engine(db_target)
    df = pd.read_csv(file_path)
    df.to_sql(name='telecom_users', con=engine, if_exists='append', index=False)

with DAG(
    dag_id='dag_rezaseptian',
    start_date=pendulum.datetime(2025, 4, 21, tz='Asia/Jakarta'),
    schedule_interval=None,
    catchup=False,
    max_active_runs=1,
    description='ETL Telecom Data to Postgres using SQLAlchemy and SQLExecuteQueryOperator',
) as dag:

    start_task = DummyOperator(task_id='start')
    end_task = DummyOperator(task_id='end')

    load_csv_task = PythonOperator(
        task_id='load_csv',
        python_callable=insert_data,
        op_kwargs={
            'file_path': path_file,
            'db_target': db_uri
        }
    )

    create_table_task = SQLExecuteQueryOperator(
    task_id='create_another_table',
    conn_id=conn_target,
    sql="""
        CREATE TABLE IF NOT EXISTS another_table (
            id INT PRIMARY KEY,
            customer_name TEXT,
            data_usage_gb FLOAT
        );
    """
)

    run_sql_filter_task = SQLExecuteQueryOperator(
        task_id='insert_filtered_data',
        conn_id=conn_target,
        sql=func.transform_query
    )

    start_task >> check_db_connection_task >> load_csv_task >> create_table_task >> run_sql_filter_task >> end_task

