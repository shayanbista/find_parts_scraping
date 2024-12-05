FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install beautifulsoup4 requests

CMD ["python", "main.py"]
