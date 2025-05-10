# build
FROM python:3.13.3-alpine AS builder

RUN apk add --no-cache build-base libffi-dev openssl-dev \
    && pip install --upgrade pip

WORKDIR /app
COPY requirements.txt .

RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r requirements.txt

# prod
FROM python:3.13.3-alpine AS runtime

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
# & python -m prometheus_client --port=${PROMETHEUS_PORT} --addr=127.0.0.1"]