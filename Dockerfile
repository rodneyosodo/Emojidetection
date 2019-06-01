FROM debian:stable-slim
LABEL name="b1ackdot"

# basic python installation
RUN apt-get update 
RUN apt-get install -y python python-dev python-pip

# Opencv installation
RUN apt-get install -y python-opencv
# application folder
RUN mkdir App
COPY . /App
WORKDIR /App

# package installations
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
