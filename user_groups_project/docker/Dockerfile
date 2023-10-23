FROM python:3.10.0-slim-buster

COPY requirements.txt /app/
WORKDIR /app
RUN apt-get update && apt-get install -y pkg-config libmariadb-dev-compat gcc
RUN pip install -r requirements.txt
COPY . /app/

CMD ./wait-for-it.sh db:3306 -- python3 manage.py runserver 0.0.0.0:8080

