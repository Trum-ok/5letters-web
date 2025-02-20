# build
FROM python:3.12.5-alpine AS builder

RUN apk add --no-cache curl

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --user -r requirements.txt

# prod
FROM python:3.12.5-alpine

WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY . .

RUN pip install --no-cache-dir gunicorn

ARG GUNICORN_PORT PROMETHEUS_PORT
ENV GUNICORN_PORT=${GUNICORN_PORT} \
    PROMETHEUS_PORT=${PROMETHEUS_PORT} \
    GUNICORN_CMD_ARGS="--workers=4 --bind=0.0.0.0:${GUNICORN_PORT} --access-logfile=-"

COPY russian_words.txt .
COPY . .

CMD ["sh", "-c", "gunicorn app:app ${GUNICORN_CMD_ARGS}"]