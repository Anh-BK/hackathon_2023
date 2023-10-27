FROM python:3.9.16-slim-buster

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    dpkg-sig \
    python3-dev 


RUN pip3 install --upgrade pip

WORKDIR /app

COPY requirements/requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY src/ .

COPY .env .env

ENV PYTHONPATH="$PYTHONPATH:/app"

WORKDIR /app/app

CMD [ "python", "main.py"]