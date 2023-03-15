SHELL := /bin/bash

.PHONY: pipenv-env
pipenv-env: ## Create python environment
	pip install --upgrade pip
	pip install pipenv
	pipenv shell

.PHONY: install
install: ## Install project dependencies
	pipenv install --dev

.PHONY: tests
tests: ## Execute unit tests
	pytest tests

.PHONY: lint
lint: ## Check lint
	pylint src/

.PHONY: black
black: ## Format code with black
	black src/

.PHONY: coverage
coverage: ## Run and report tests coverage
	pytest --cov tests
	
.PHONY: docker-build
docker-build: ## Build docker images
	docker-compose build

.PHONY: docker-run
docker-run: ## Run docker containers
	docker-compose up -d

.PHONY: generate-migrations
generate-migrations: ## Generate migrations using Alembic
	docker-compose run --rm fastapi-ddd alembic revision --autogenerate -m "create inital tables"

.PHONY: apply-migrations
apply-migrations: ## Apply the generated migration to database
	docker-compose run --rm fastapi-ddd alembic upgrade head

.PHONY: help
help:
	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ \
	{ printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) }\
	 ' $(MAKEFILE_LIST)
