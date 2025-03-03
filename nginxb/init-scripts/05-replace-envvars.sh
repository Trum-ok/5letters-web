#!/usr/bin/env sh

set -e

TEMPLATES=/etc/nginx/templates

if [ ! -f "$TEMPLATES"/nginx.conf.template ]; then
    echo "nginx.conf.template does not exist in ${TEMPLATES}";
    exit 1
fi

envsubst '${SERVER_NAME} ${GUNICORN_PORT} ${PROMETHEUS_PORT}' \
    < /etc/nginx/templates/nginx.conf.template \
    > /etc/nginx/nginx.conf

if [ ! -f "$TEMPLATES"/app.conf.template ]; then
    echo "app.conf.template does not exist in ${TEMPLATES}";
    exit 1
fi

envsubst '${SERVER_NAME} ${GUNICORN_PORT} ${PROMETHEUS_PORT}' \
    < /etc/nginx/templates/app.conf.template \
    > /etc/nginx/conf.d/app.conf

rm -f /etc/nginx/templates/nginx.conf.template
rm -f /etc/nginx/templates/app.conf.template

# cat /etc/nginx/nginx.conf
# echo
# cat /etc/nginx/conf.d/app.conf
# echo

exec "$@"