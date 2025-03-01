FROM nginx:1.27.4-alpine

RUN mkdir -p /etc/nginx/templates
RUN rm -rf /etc/nginx/conf.d/*

RUN apk add --no-cache gettext && \
    adduser -D -u 1001 -g 'nginx' -s /bin/false nginxuser

COPY ssl/ /etc/nginx/ssl/

RUN chown -R nginxuser:nginx /etc/nginx && \
    chmod 755 /etc/nginx && \
    chmod 600 /etc/nginx/ssl/*.key && \
    chmod 644 /etc/nginx/ssl/*.crt

COPY nginxb/templates/nginx.conf.template /etc/nginx/templates/nginx.conf.template
COPY nginxb/templates/app.conf.template /etc/nginx/templates/app.conf.template
COPY nginxb/init-scripts/ /docker-entrypoint.d/

RUN chmod +x /docker-entrypoint.d/*.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]