FROM python:3.8-alpine3.10

ENV PYTHONPATH=.

RUN apk add binutils libc-dev

RUN mkdir /app
COPY . /app

WORKDIR /app
RUN pip install -r requirements.txt

CMD gunicorn 'app:create_app()' --bind 0.0.0.0:5000
