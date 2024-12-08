FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install sqlalchemy

EXPOSE 8000

CMD ["python3", "-m", "http.server", "--cgi", "8000"]
