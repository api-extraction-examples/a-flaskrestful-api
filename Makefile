DOCKER_IMAGE_NAME = a-flaskrestful-api
DOCKER_CONTAINER_NAME = container-$(DOCKER_IMAGE_NAME)

all: build_docker

run:
	python run.py

reset_docker:
	-docker stop $(DOCKER_CONTAINER_NAME)
	-docker rm $(DOCKER_CONTAINER_NAME)
	-docker rmi $(DOCKER_IMAGE_NAME)

build_docker: reset_docker
	@echo "Building image: $(DOCKER_IMAGE_NAME)"
	docker build -t $(DOCKER_IMAGE_NAME) .

run_docker: build_docker
	@echo "Starting container: $(DOCKER_CONTAINER_NAME)"
	#docker run --name $(DOCKER_CONTAINER_NAME) -p 8009:8009 -v $(PWD)/:/a-flaskrestful-api -d -i -t $(DOCKER_IMAGE_NAME) /bin/sh
	docker run --name $(DOCKER_CONTAINER_NAME) -p 8009:8009 -v $(PWD)/:/a-flaskrestful-api -d -i -t $(DOCKER_IMAGE_NAME)
	@echo "Container '$(DOCKER_CONTAINER_NAME)' started"

enter_docker_container:
	docker exec -it $(DOCKER_CONTAINER_NAME) bash
