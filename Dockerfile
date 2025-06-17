FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y gcc libpq-dev \
    && pip install --upgrade pip \
    && pip install -r requirements.txt
    

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
