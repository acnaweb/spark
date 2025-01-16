# Projeto 3 - Apache Airflow e Apache Spark Para Extração e Processamento de Dados em Tempo Real
# DAG Para SparkSubmitOperator

# Imports
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime, timedelta

# Argumentos
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# DAG
dag_operador_spark = DAG(
    dag_id = 'dag-dsa-projeto3-conn',
    default_args = default_args,
    description = 'DAG para executar job Spark via Operador Spark',
    catchup = False,
    schedule_interval = '@daily',
    tags = ["spark-submit", "spark-connection"]
)

# Tarefa
spark_task = SparkSubmitOperator(

    # Id da tarefa
    task_id = 'tarefa-dag-dsa-projeto3-conn',

    # Conexão criada no Airflow
    conn_id = 'spark_default',  

    # Caminho para o job Spark
    application = '/opt/airflow/spark_scripts/projeto3.py',  

    # Nome da app Spark
    name = 'DSASparkJob',  
    verbose = False,

    # Spark Master URL
    conf = {'spark.master': 'spark://spark-master:7077'},  

    # DAG
    dag = dag_operador_spark,
)


