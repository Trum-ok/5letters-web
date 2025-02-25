FROM nginx:1.27.4-alpine

RUN rm -rf /etc/nginx/conf.d/*

RUN apk add --no-cache gettext && \
    adduser -D -u 1001 -g 'nginx' -s /bin/false nginxuser

COPY templates/nginx.conf.template /etc/nginx/templates/
COPY ssl/ /etc/nginx/ssl/

RUN chown -R nginxuser:nginx /etc/nginx && \
    chmod 755 /etc/nginx && \
    chmod 600 /etc/nginx/ssl/*.key && \
    chmod 644 /etc/nginx/ssl/*.crt

CMD ["sh", "-c", \
    "envsubst '$$GUNICORN_PORT $$PROMETHEUS_PORT' < /etc/nginx/templates/nginx.conf.template \
     > /etc/nginx/conf.d/app.conf && exec nginx -g 'daemon off;'"]
