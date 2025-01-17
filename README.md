# Spark

## Modules

### Spark Submit

```sh
docker exec spark-master spark-submit --deploy-mode client /opt/spark/apps/sql/projeto1-tarefa1.py
docker exec spark-master spark-submit --deploy-mode client /opt/spark/apps/sql/projeto1-tarefa2.py
docker exec spark-master spark-submit --deploy-mode client /opt/spark/apps/sql/projeto1-tarefa3.py
docker exec spark-master spark-submit --deploy-mode client /opt/spark/apps/sql/projeto1-tarefa4.py
docker exec spark-master spark-submit --deploy-mode client /opt/spark/apps/sql/projeto1-tarefa5.py

docker exec spark-master spark-submit --deploy-mode cluster /opt/spark/apps/sql/projeto1-tarefa1.py
```

### Spark SQL

```python

```

## Install & Config

### Setup

- .env.spark

```sh
SPARK_NO_DAEMONIZE=true
```

### Run

```sh
docker compose -f ./docker/custom/compose.yml up --build --scale spark-worker=5
```

### Navigate

-  Spark Master

http://localhost:9090

-  History Server

http://localhost:18080


## References
