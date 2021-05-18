FROM python:3.9-slim-buster

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=0 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get -o Dpkg::Options::='--force-confmiss' install -y --no-install-recommends netbase build-essential libev-dev && \
    pip install -r requirements.txt && \
    rm -r /root/.cache/pip && \
    apt-get remove -y --purge build-essential && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

COPY app app
COPY gunicorn_config.py .

EXPOSE 8000
