# Use an official Python runtime as a parent image
FROM python:2.7

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
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
	libmysqlclient-dev \
	libpq-dev \
	sqlite3 && \
	pip install -U pip setuptools && \
  	rm -rf /var/lib/apt/lists/*

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8000
# Define environment variable

RUN chmod +x entry_point.sh

# Run app.py when the container launches
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#
#CMD ["python", "manage.py", "migrate"]
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

#CMD ["uwsgi", "uwsgi.ini"]