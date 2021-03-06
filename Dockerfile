FROM python:3.6.4-alpine

RUN apk update \
  && apk add \
    build-base

RUN pip install --upgrade pip \
  && pip install pytest

RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY ./requirements.txt .
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED 1

COPY . .