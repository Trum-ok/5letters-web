# build
FROM python:3.12.5-alpine AS builder

RUN apk add --no-cache curl

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --user -r requirements.txt
# RUN mkdir -p /var/log/flask && chmod 777 /var/log/flask

# prod
FROM python:3.12.5-alpine

WORKDIR /app

COPY gunicorn.conf.py ./gunicorn.conf.py
COPY --from=builder /root/.local /root/.local
COPY . .

RUN pip install --no-cache-dir gunicorn

ARG GUNICORN_PORT PROMETHEUS_PORT
ENV GUNICORN_PORT=${GUNICORN_PORT} \
    PROMETHEUS_PORT=${PROMETHEUS_PORT}

COPY russian_words.txt .
COPY . .

CMD ["sh", "-c", "gunicorn app:app -c gunicorn.conf.py"]
# CMD ["sh", "-c", "gunicorn app:app ${GUNICORN_CMD_ARGS} & python -m prometheus_client --port=${PROMETHEUS_PORT} --addr=127.0.0.1"]