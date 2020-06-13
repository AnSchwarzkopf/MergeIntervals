FROM ubuntu:20.10
COPY requirements.txt requirements.txt 
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3 \
    build-essential \
    && pip3 install -r requirements.txt