FROM python:3.12-slim

WORKDIR /opt/taimu

COPY ./requirements /opt/taimu/requirements

RUN pip install --no-cache-dir --upgrade -r /opt/taimu/requirements/dev.txt

COPY ./src /opt/taimu/src
