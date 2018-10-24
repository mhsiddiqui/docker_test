# Use an official Python runtime as a parent image
FROM python:2.7

WORKDIR /app

ADD . /app

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    apt-utils \
	git \
	python \
	python-dev \
	libpcre3 \
	libpcre3-dev \
	python-setuptools \
	python-pip \
	nginx \
	supervisor \
	default-libmysqlclient-dev \
	python-psycopg2 \
	libpq-dev \
	sqlite3 && \
	pip install -U pip setuptools && \
  	rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt

RUN chmod +x entry_point.sh

EXPOSE 8000


