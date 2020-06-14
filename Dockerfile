FROM python:3.8-slim
COPY requirements.txt requirements.txt
RUN apt-get update \
    && pip3 install -r requirements.txt