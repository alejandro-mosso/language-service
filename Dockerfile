FROM amancevice/pandas:1.0.0
#FROM python:3.7-alpine

MAINTAINER Alejandro Mosso.

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    DJANGO_SETTINGS_MODULE=config.settings.production \
    PORT=9000 \
    WEB_CONCURRENCY=3

EXPOSE 9000

# Install dependencies
USER root
# RUN apt-get install python-lxml
#    libwebp-dev libjpeg zlib


COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Setup directory structure
RUN mkdir /app
WORKDIR /app
COPY ./app/app /app

