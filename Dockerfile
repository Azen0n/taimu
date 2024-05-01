FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1

WORKDIR /opt/taimu

COPY ./requirements.txt /opt/taimu/requirements.txt
COPY ./pyproject.toml /opt/taimu/pyproject.toml

RUN pip install --no-cache-dir --upgrade -r /opt/taimu/requirements.txt

COPY ./src /opt/taimu/src
