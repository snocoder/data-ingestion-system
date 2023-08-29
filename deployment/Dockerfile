FROM ubuntu:22.04
ENV PYTHONUNBUFFERED 1
ENV PYTHONIOENCODING UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_TYPE en_US.UTF-8

RUN apt-get update
RUN apt-get install -y python3.10
RUN apt-get install -y python3-pip
RUN apt-get install -y libpq-dev
RUN apt-get install -y gcc

RUN mkdir /config
ADD requirements.txt /config/requirements.txt
RUN pip3 install -r /config/requirements.txt

RUN mkdir -p /src
WORKDIR /src
COPY ./ ./