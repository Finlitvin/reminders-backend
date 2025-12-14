app-name ?= reminders_backend
host ?= 0.0.0.0
port ?= 8000
lint-dir ?= .


.PHONY: help
help: ## Generates a help README
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


.PHONY: serve
serve: ## Run app (Uvicorn, uvloop)
	uvicorn src.backend:app --host $(host) --port $(port) --reload --loop uvloop


##################################### Lint #####################################
.PHONY: check
check: ## Check code (Ruff)
	uv tool run ruff check $(lint-dir) --fix


.PHONY: format
format: ## Format code (Ruff)
	uv tool run ruff format $(lint-dir)


.PHONY: lint
lint: ## Check and format code (Ruff)
	make check ; make format


##################################### Docker #####################################
.PHONY: prune
prune: ## reset docker system
	sudo docker system prune -af --volumes

.PHONY: up
up: ## up all services in docker
	sudo docker-compose up -d --build

.PHONY: down
down: ## down all services in docker
	sudo docker-compose down

.PHONY: env
env: ## eport var from env file
	export $(cat .env)
