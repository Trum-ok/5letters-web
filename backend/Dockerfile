FROM python:3.11.1-alpine
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY russian_words.txt .
COPY . .

EXPOSE 8080

CMD ["python", "app.py"]