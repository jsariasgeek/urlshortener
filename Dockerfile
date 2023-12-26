FROM python:3.8.12-alpine
WORKDIR /app
COPY requirements.txt /app/
RUN apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install debugpy
COPY . /app/
# EXPOSE 8078
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8078"]

# how can i start this on my local machine mapping 8078:8078 and with container name trading-journal?
# docker run -p 8078:8078 trading-journal 