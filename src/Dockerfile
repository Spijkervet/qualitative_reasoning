FROM python:3
COPY . /app
WORKDIR /app

RUN apt-get update -y && apt-get install graphviz -y
RUN pip3 install pydot
