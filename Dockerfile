
FROM ubuntu: latest

LABEL maintainer='Evan (Evangellos) Wiegers'

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

RUN apt-get update -y && \
	apt-get install dialog apt-utils -y && \
	apt-get install  -y software-properties-common

RUN apt-get install -y python3-pip
RUN python3 -m pip install pynput && \
	python3 -m pip install pyqrcode pypng qrtools && \
	python3 -m pip install stegano

ENTRYPOINT ["/bin/bash"]