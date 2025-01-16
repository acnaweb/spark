# Projeto 3 - Apache Airflow e Apache Spark Para Extração e Processamento de Dados em Tempo Real
# Script ETL

# Imports
import json
import requests
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Função para obter os dados
def dsa_get_dados_api(url):

    # Faz requisição à URL
    response = requests.get(url)

    # Status 200 indica sucesso
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro ao obter os dados de {url}")

# Função para processar os dados
def dsa_processa_dados(data):

    # Faz o dump dos dados e salva em disco
    with open("api_data.json", "w") as data_file:
        json.dump(data, data_file)

    # Cria sessão Spark
    spark = SparkSession.builder.appName("DSAProjeto3").getOrCreate()
    
    # Carrega o arquivo do disco
    dsa_json_dataframe = spark.read.json("api_data.json")
    
    # Expande (explode) a coluna data, filtra os dados e gera a saída
    dataframe = dsa_json_dataframe.withColumn("data", F.explode("data")).select("data.*", "meta.*")

    return dataframe

# Função para salvar os dados
def dsa_salva_dados(dataframe, output_path):
    dataframe.repartition(1).write.format('json').mode('overwrite').save(output_path)

# Bloco principal
if __name__ == "__main__":

    # URL da fonte de dados    
    url = "https://api.mfapi.in/mf/118550"

    # Pasta de saída é a pasta corrente
    output_path = "."
    
    # Bloco try/except
    try:

        # Obtém os dados
        data = dsa_get_dados_api(url)

        # Processa os dados
        dataframe = dsa_processa_dados(data)

        # Salva o resultado
        dsa_salva_dados(dataframe, output_path)

    except Exception as e:

        print(f"Error: {e}")


