.DEFAULT_GOAL := help

ifeq ($(OS),Windows_NT)
	APP_DIR := "$(shell powershell "(New-Object -ComObject Scripting.FileSystemObject).GetFolder('.').ShortPath")"
else
	APP_DIR := "$$(pwd)"
endif

PROJECT_IMAGE_NAME := "flask-api-app"

.PHONY: base-build
base-build:
	docker build -t $(PROJECT_IMAGE_NAME) .

.PHONY: base-interactive
base-interactive:
	docker run -it --workdir="/src" -v $(APP_DIR):/src $(PROJECT_IMAGE_NAME) /bin/bash

.PHONY: dependencies-install
dependencies-install:
	docker run -it --workdir="/src" -v $(APP_DIR):/src $(PROJECT_IMAGE_NAME) /bin/bash -ci "poetry install"

.PHONY: dependencies-update
dependencies-update:
	docker run -it --workdir="/src" -v $(APP_DIR):/src $(PROJECT_IMAGE_NAME) /bin/bash -ci "poetry update --lock"

.PHONY: dependencies-add-package
PACK_NAME ?= 'flask==2.3.2'
dependencies-add-package:
	docker run -it --workdir="/src" -v $(APP_DIR):/src $(PROJECT_IMAGE_NAME) /bin/bash -ci "poetry update add $(PACK_NAME)"

.PHONY: flask-run-app
PORT ?= 5000
flask-run-app:
	docker run -t --rm --env-file=.env --workdir="/src" -p $(PORT):$(PORT) -v $(APP_DIR):/src $(PROJECT_IMAGE_NAME) /bin/bash -ci "python src/app.py"

.PHONY: docker-clean
docker-clean:
ifeq ($(OS),Windows_NT)
	powershell "docker ps -qa | %{docker kill $$_}; docker container prune --force; docker system prune --force"
else
	docker ps -qa | xargs docker kill; docker container prune --force; docker system prune --force;
endif