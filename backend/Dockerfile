FROM python:3.12.5-alpine

ARG FLASK_PORT=8080
ENV FLASK_PORT=${FLASK_PORT}
ARG PROMETHEUS_PORT=5001
ENV PROMETHEUS_PORT=${PROMETHEUS_PORT}

RUN apk add --no-cache curl

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY russian_words.txt .
COPY . .

CMD ["sh", "-c", "python app.py --port ${FLASK_PORT} --promport ${PROMETHEUS_PORT}"]