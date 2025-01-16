# Spart

docker run \
--volume ./lab/spark-cluster/spark-jobs/p3_etl_script.py:/opt/bitnami/spark/job.py  \
bitnami/spark:latest \
spark-submit --master spark-master:7077 --conf spark.master=spark://spark-master:7077 --name DSASparkJob

spark-submit --master spark-master:7077 --conf spark.master=spark://spark-master:7077 --principal alunodsa --name DSASparkJob --queue root.default --deploy-mode client /opt/***/spark_scripts/projeto3.py. Error code is: 2.; 745)

```sh
docker run bitnami/spark:latest spark-submit --help
```

```sh
docker run bitnami/spark:latest \
spark-submit \
--master spark://host.docker.internal:7077 \
--conf spark.master=spark://host.docker.internal:7077 \
--principal alunodsa \
--name myjob \
--queue root.default \
--deploy-mode client
```

spark-submit --master spark-master:7077 --conf spark.master=spark://spark-master:7077 --principal alunodsa --name DSASparkJob --queue root.default --deploy-mode client /opt/***/spark_scripts/projeto3.py

## References


- https://spark.apache.org/

- https://superuser.com/questions/816143/how-to-run-pip-in-non-interactive-mode
- https://docs.pytest.org/en/stable/reference/customize.html
- https://www.activestate.com/resources/quick-reads/how-to-manually-install-python-packages/
- https://sparkbyexamples.com/spark/spark-submit-command/