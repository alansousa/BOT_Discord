FROM python:3.10.7-slim-buster

RUN apt update -y && apt upgrade -y && apt install ffmpeg -y

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

cmd ["python", "main.py"]