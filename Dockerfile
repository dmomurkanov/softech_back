# Base image
FROM python:3.11-alpine AS base

# Install required system dependencies
RUN apk add --no-cache gcc musl-dev libffi-dev


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

EXPOSE 8000

# Install poetry
RUN pip install --no-cache-dir poetry

ADD ./requirements.txt /app/requirements.txt
RUN pip install -U pip && pip install -r requirements.txt
ADD . /app
