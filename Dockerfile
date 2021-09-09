FROM python:3.8.7-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN DEBIAN_FRONTEND=noninteractive apt-get update --fix-missing
RUN DEBIAN_FRONTEND=noninteractive apt-get install apt-utils libsm6 libxext6 ghostscript cron -y

# install dependencies
RUN pip install --upgrade pip
RUN pip install openpyxl

COPY ./.env.example /usr/src/app/.env
COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt --no-cache-dir

# copy project
COPY . /usr/src/app/