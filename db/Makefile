.DEFAULT_GOAL := help

ifeq ($(OS),Windows_NT)
	APP_DIR := "$(shell powershell "(New-Object -ComObject Scripting.FileSystemObject).GetFolder('.').ShortPath")"
else
	APP_DIR := "$$(pwd)"
endif

PROJECT_IMAGE_NAME := "postgres-db"
WORK_DIR := dba

.PHONY: base-build
base-build:
	docker build -t $(PROJECT_IMAGE_NAME) .

.PHONY: base-interactive
base-interactive:
	docker run -it --workdir=/$(WORK_DIR) -v $(APP_DIR):/$(WORK_DIR) $(PROJECT_IMAGE_NAME) /bin/bash

.PHONY: base-run
base-run:
	docker run -d -e POSTGRES_PASSWORD=jose $(PROJECT_IMAGE_NAME)