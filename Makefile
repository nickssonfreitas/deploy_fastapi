IMAGE_NAME=deploy_fastapi
CONTAINER_NAME=fastapi_container

build:
	docker-compose build

run:
	docker-compose up

stop:
	docker-compose down

logs:
	docker-compose logs -f

.PHONY: build run stop logs
