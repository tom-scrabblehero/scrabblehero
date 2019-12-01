FROM python:3.8-alpine3.10

ENV PYTHONPATH=.
ENV PORT=5000

RUN apk add binutils libc-dev postgresql-dev gcc

RUN mkdir /app
COPY . /app

WORKDIR /app
RUN pip install -r requirements.txt

CMD gunicorn 'app:create_app()' --bind 0.0.0.0:$PORT
