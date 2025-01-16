run_custom:
	docker compose -f ./docker/custom/compose.yml up --build --scale spark-worker=5

