run_custom:
	docker compose -f ./docker/custom/compose.yml up --build --scale spark-worker=3

run_bitnami:
	docker compose -f ./docker/bitnami/compose.yaml up --scale spark-worker=3

