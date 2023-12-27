FROM python:3.8.12-alpine
WORKDIR /app
COPY requirements.txt /app/
RUN apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install debugpy
COPY . /app/
