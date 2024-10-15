FROM python:3.10.6-alpine3.16

COPY requirements.txt /temp/requirements.txt
COPY wishlists_project /wishlists_project
WORKDIR /wishlists_project
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password admin

USER admin