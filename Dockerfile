# Use an official Python runtime as a parent image
FROM python:3.12-slim-bookworm

WORKDIR /app

COPY . /app

# Install system updates and dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=application.py

CMD ["python", "application.py"]