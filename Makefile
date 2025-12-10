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


.PHONY: build
build: ## Build docker image (Docker)
	sudo docker build . --tag $(app-name) \
	--build-arg DB_HOST=$(DB_HOST) \
	--build-arg DB_NAME=$(DB_NAME) \
	--build-arg DB_USER=$(DB_USER) \
	--build-arg DB_PASSWORD=$(DB_PASSWORD) \


.PHONY: run
run: ## Run docker container (Docker)
	sudo docker run \
	-d -p $(port):$(port) \
	--name $(app-name) $(app-name) \


.PHONY: log
log: ## Container log (Docker)
	sudo docker logs $(app-name) -f -n 1000


.PHONY: stop
stop: ## Stop docker container (Docker)
	sudo docker stop $(app-name)


.PHONY: rm
rm: ## Delete docker container (Docker)
	sudo docker rm $(app-name)


.PHONY: rmi
rmi: ## Delete docker image (Docker)
	sudo docker rmi $(app-name)


.PHONY: dserve
dserve: ## Build and run and log (Docker)
	make build && make run && make log


.PHONY: flush
flush: ## Stop and rm\rmi (Docker)
	make stop ; make rm ; make rmi


.PHONY: env
env: ## eport var from env file
	export $(cat .env)