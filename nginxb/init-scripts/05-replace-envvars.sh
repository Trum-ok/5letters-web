#!/usr/bin/env sh

set -e

envsubst '${SERVER_NAME} ${GUNICORN_PORT} ${PROMETHEUS_PORT}' \
    < /etc/nginx/templates/nginx.conf.template \
    > /etc/nginx/nginx.conf

envsubst '${SERVER_NAME} ${GUNICORN_PORT} ${PROMETHEUS_PORT}' \
    < /etc/nginx/templates/app.conf.template \
    > /etc/nginx/conf.d/app.conf

rm -rf /etc/nginx/templates

cat /etc/nginx/nginx.conf
echo
cat /etc/nginx/conf.d/app.conf
echo

exec "$@"