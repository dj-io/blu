# get image we want
FROM python:3.12-slim

# set env variables
ENV PYTHONUNBUFFERED=1

# create working directory for our app
WORKDIR /app

# install all deps on to our container
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

# move all code into our container directory
COPY . /app
RUN mkdir -p /certs

# export a port to access the app in our container
EXPOSE 8000
