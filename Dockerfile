FROM python:3.6-alpine
RUN  apk add --no-cache --virtual gcc
WORKDIR /code/

COPY requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir

ENV PYTHONPATH /code
COPY . .
CMD gunicorn -w 1 -b 0.0.0.0:80 server:app

