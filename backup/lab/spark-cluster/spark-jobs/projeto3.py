# Projeto 3 - Apache Airflow e Apache Spark Para Extração e Processamento de Dados em Tempo Real
# Spark Job

# Importa o módulo airflow para uso geral no script
import airflow

# Importa timedelta do módulo datetime para definir intervalos de tempo
from datetime import timedelta

# Importa DAG do módulo airflow para definir um Directed Acyclic Graph
from airflow import DAG

# Importa SparkSubmitOperator de airflow.providers.apache.spark.operators.spark_submit para submissão de trabalhos Spark
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator 

# Importa days_ago de airflow.utils.dates para cálculo de datas passadas
from airflow.utils.dates import days_ago

# Define os argumentos padrão para serem aplicados ao DAG
default_args = {

    # Define o proprietário do DAG
    'owner': 'airflow',    

    # Define o tempo de espera antes de tentar uma nova execução após falha
    'retry_delay': timedelta(minutes=5),  
}

# Cria uma instância de um DAG com configurações específicas
spark_dag = DAG(

        # Identificador único para o DAG
        dag_id = "spark_airflow_dag",  

        # Aplica os argumentos padrão definidos anteriormente
        default_args = default_args,  

        # Define que o DAG não possui uma programação fixa de execução
        schedule_interval = None,  

        # Tempo máximo de execução permitido para uma execução do DAG
        dagrun_timeout = timedelta(minutes=60),  

        # Descrição do propósito do DAG
        description = 'SparkSubmitOperator no airflow', 

        # Define a data de início das execuções do DAG como um dia atrás 
        start_date = airflow.utils.dates.days_ago(1)  
)

# Define uma tarefa no DAG para submeter um script Spark usando SparkSubmitOperator
processo_etl = SparkSubmitOperator(

        # Caminho para o script Spark a ser executado
        application = './p3_etl_script.py',  

         # Identificador da conexão Spark a ser utilizada
        conn_id = 'spark_default', 

        # Identificador único para a tarefa dentro do DAG
        task_id = 'spark_submit_task',  

        # Associa esta tarefa ao DAG definido anteriormente
        dag = spark_dag  
)

processo_etl


