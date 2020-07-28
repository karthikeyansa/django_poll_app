FROM python:3

ENV PYTHONBUFFERED 1

RUN mkdir /poll

WORKDIR /poll

ADD requirements.txt /poll/

RUN pip install -r requirements.txt

ADD . /poll/