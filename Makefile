export IMAGE_NAME=my-image

# Local development
install:
	python -m venv venv; \
	. venv/bin/activate; \
	pip install --upgrade pip; \
	pip install pre-commit; \
	pip install -e .[interactive]; \
	pre-commit install; \
	git config --bool flake8.strict true; \

run_spark:
	cd server; \
	docker compose up -d; \

stop_spark:
	cd server; \
	docker compose stop; \

info:
	docker logs server-spark-master-1

run:
	python main.py
