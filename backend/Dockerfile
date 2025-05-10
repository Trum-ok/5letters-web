# build
FROM python:3.13.3-alpine AS builder

RUN apk add --no-cache build-base libffi-dev openssl-dev \
    && pip install --upgrade pip

WORKDIR /app
COPY requirements.txt .

RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r requirements.txt

# prod
FROM python:3.13.3-alpine AS runtime
RUN apk add --no-cache libffi openssl \
    && adduser -D -u 1000 fastapiuser

WORKDIR /app

COPY --from=builder /wheels /wheels
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade \
        --find-links=/wheels -r requirements.txt \
    && pip install --no-cache-dir uvicorn[standard] \
    && rm -rf /wheels

COPY . .

RUN chown -R fastapiuser:fastapiuser /app
USER fastapiuser

ARG APP_PORT=8000
ARG PROMETHEUS_PORT=8001

ENV APP_PORT=${APP_PORT} \
    PROMETHEUS_PORT=${PROMETHEUS_PORT} \
    PATH="/home/fastapiuser/.local/bin:$PATH"

COPY russian_words.txt .

EXPOSE ${APP_PORT} ${PROMETHEUS_PORT}

CMD ["sh","-c","uvicorn app:app --host 0.0.0.0 --port $APP_PORT"]
