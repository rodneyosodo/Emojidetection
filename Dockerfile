FROM debian:stable-slim
MAINTAINER b1ackdot <b1ackd0t@protonmail.com>

# basic python installation
RUN apt-get update 
RUN apt-get install -y python python-dev python-pip

# application folder
RUN mkdir App
COPY . /App
WORKDIR /App

# package installations
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
