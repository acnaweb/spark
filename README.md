# Spark

### Operate

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
