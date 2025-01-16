# Usa a imagem do Apache Airflow como base
FROM apache/airflow:2.8.1

# Instala o provedor do Apache Spark para o Apache Airflow
RUN pip install apache-airflow-providers-apache-spark

# Muda o usuário para root para instalar pacotes adicionais
USER root 

# Atualiza os pacotes do sistema e instala o Java Runtime Environment (JRE), Java Development Kit (JDK) e o servidor SSH
RUN apt-get update -y && apt install default-jre default-jdk openssh-server -y

# Define a versão do Spark a ser instalada
ENV SPARK_VERSION 3.5.0

# Define o diretório onde o Spark será instalado
ENV SPARK_HOME /usr/local/share/spark

# Baixa e extrai o Spark no diretório especificado
RUN curl -fL "https://archive.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop3.tgz" | tar xfz - -C /usr/local/share && \
    mv "/usr/local/share/spark-$SPARK_VERSION-bin-hadoop3" "$SPARK_HOME"

# Adiciona o diretório do Spark ao PATH 
ENV PATH "$PATH:$SPARK_HOME/bin"

# Copia a configuração do servidor SSH para o container
COPY ./spark-cluster/sshd_config /etc/ssh/sshd_config

# Copia a configuração do cliente SSH para o container
COPY ./spark-cluster/ssh_config /etc/ssh/ssh_config

# Muda o usuário de volta para airflow
USER airflow

# Cria um diretório para os scripts do Spark
RUN mkdir -p /opt/airflow/spark_scripts

# Copia o script do projeto Spark para o diretório criado
# COPY ./spark-cluster/spark-jobs/projeto3.py /opt/airflow/spark_scripts/

# Define o ponto de entrada para inicializar o banco de dados do Airflow e iniciar o servidor web e o agendador
ENTRYPOINT [ "bash", "-c", "/entrypoint airflow db init && (/entrypoint airflow webserver & /entrypoint airflow scheduler)" ]

# Define um comando vazio para ser substituído em tempo de execução, se necessário
CMD []
