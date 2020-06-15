FROM python:3.8-slim
COPY requirements.txt requirements.txt
RUN apt-get update \
    && apt-get install -y \
    build-essential \
    && pip3 install -r requirements.txt