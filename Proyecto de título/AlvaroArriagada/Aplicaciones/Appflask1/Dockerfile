FROM python:3.5
ADD . /code
WORKDIR /code/
RUN apt-get update 
RUN apt-get install -y python3 python3-dev python3-pip nginx 
RUN pip3 install uwsgi
RUN pip3 install -r requirements.txt

EXPOSE 5000