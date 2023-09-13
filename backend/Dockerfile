FROM python:3.11-alpine3.17

ENV PYTHONUNBUFFERED 1

WORKDIR /app/backend/

RUN apk add bash nano htop tzdata

COPY requirements.txt /app/backend/

RUN pip install -r requirements.txt

ADD . /app/backend/
