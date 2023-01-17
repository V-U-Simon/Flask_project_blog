FROM python:3.11-slim-bullseye
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY wsgi.py wsgi.py
COPY app ./app
EXPOSE 5000
CMD python wsgi.py