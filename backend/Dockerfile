FROM python:3.12.1-alpine3.19

ENV PYTHONUNBUFFERED=1

WORKDIR /app/backend/

RUN apk add bash nano htop tzdata

COPY requirements.txt /app/backend/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
