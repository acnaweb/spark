# Usa a imagem do OpenJDK 8 como base
FROM openjdk:8

# Define a versão do Spark a ser instalada
ENV SPARK_VERSION 3.5.0

# Define o diretório onde o Spark será instalado
ENV SPARK_HOME /usr/local/share/spark

# Baixa e extrai o Spark no diretório especificado
RUN curl -fL "https://archive.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop3.tgz" | tar xfz - -C /usr/local/share && \
    mv "/usr/local/share/spark-$SPARK_VERSION-bin-hadoop3" "$SPARK_HOME"

# Adiciona o diretório do Spark ao PATH para facilitar a execução de comandos do Spark
ENV PATH "$PATH:$SPARK_HOME/bin"

# Atualiza os pacotes do sistema e instala o servidor SSH
RUN apt-get update && apt-get install -y openssh-server

# Copia a configuração do servidor SSH para o container
COPY sshd_config /etc/ssh/sshd_config

# Copia a configuração do cliente SSH para o container
COPY ssh_config /etc/ssh/ssh_config

# Copia o arquivo de configuração do ambiente Spark para o container
COPY spark-env.sh /usr/local/share/spark/conf/spark-env.sh

# Copia a lista de workers do Spark para o container
COPY slaves /usr/local/share/spark/conf/slaves

# Define o comando padrão para iniciar o servidor SSH e os serviços do Spark
CMD ["sh", "-c", "service ssh start && sh -c /usr/local/share/spark/sbin/start-master.sh && sh -c /usr/local/share/spark/sbin/start-thriftserver.sh && sh -c /usr/local/share/spark/sbin/start-all.sh && tail -f /dev/null"]