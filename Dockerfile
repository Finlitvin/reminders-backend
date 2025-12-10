FROM python:3.13.5-slim-bookworm

LABEL maintainer="Rostislav <rlitvenkov@icloud.com>"
LABEL description="reminders_backend"
LABEL version="0.0.1"

ENV APP_PATH=/reminders_backend
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

ARG DB_HOST
ARG DB_NAME
ARG DB_USER
ARG DB_PASSWORD

RUN apt-get update &&\
    apt-get upgrade -y &&\
    apt-get install -y git

COPY --from=ghcr.io/astral-sh/uv:0.7.8 /uv /uvx /bin/

WORKDIR $APP_PATH

COPY . $APP_PATH
RUN uv sync --locked

ENV PATH="$APP_PATH/.venv/bin:$PATH"

RUN echo "DB_HOST=$DB_HOST" >> .env &&\
    echo "DB_NAME=$DB_NAME" >> .env &&\
    echo "DB_USER=$DB_USER" >> .env &&\
    echo "DB_PASSWORD=$DB_PASSWORD" >> .env

EXPOSE 8000

ENTRYPOINT ["uvicorn", "src.backend:app", "--host", "0.0.0.0", "--port", "8000", "--reload", "--loop", "uvloop"]