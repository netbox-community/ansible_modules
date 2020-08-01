FROM python:3.6-slim

ENV PYTHONUNBUFFERED=1

RUN apt-get update -y && \
    apt-get install -y build-essential

RUN pip install --upgrade pip poetry

COPY ./pyproject.toml ./pyproject.toml

RUN poetry config virtualenvs.create false && \
    poetry install

COPY . /app
WORKDIR /app
RUN chown -R root:root /app/docs/plugins
RUN chmod -R 644 /app/docs/plugins/

RUN ansible-galaxy collection build . && \
    ansible-galaxy collection install netbox*.tar.gz
