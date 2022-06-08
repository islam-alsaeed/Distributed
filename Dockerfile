FROM python:3.9
ENV PYTHONUNBUFFERED=1 
WORKDIR /project

COPY requirements.txt ./

RUN pip3 install -r requirements.txt
