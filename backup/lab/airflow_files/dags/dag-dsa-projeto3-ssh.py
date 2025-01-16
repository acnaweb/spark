# Projeto 3 - Apache Airflow e Apache Spark Para Extração e Processamento de Dados em Tempo Real
# DAG Para SSHOperator

# # Imports
from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.ssh.operators.ssh import SSHOperator

# Argumentos
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# DAG
dag_operador_ssh = DAG(
    dag_id = 'dag-dsa-projeto3-ssh',
    default_args = default_args,
    description = 'DAG para executar job Spark via Operador SSH',
    catchup = False,
    schedule_interval = '@daily',
    tags = ["spark-submit", "ssh"]
)

ssh_task = SSHOperator(
    task_id = 'tarefa-dag-dsa-projeto3-ssh',
    ssh_conn_id = 'ssh_default', 
    command = 'export PATH=/usr/local/openjdk-8/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/share/spark/bin; spark-submit --master spark://spark-master:7077 --conf spark.master=spark://spark-master:7077 --name DSASparkJob --queue root.default --deploy-mode client /home/projeto3.py',
    dag = dag_operador_ssh,
)
