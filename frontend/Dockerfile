# build
FROM node:20.18.3-alpine AS builder

ARG VITE_BACK_PORT
ENV VITE_BACK_PORT=$VITE_BACK_PORT

WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --silent
COPY . .
RUN npm run build

# prod
FROM nginx:1.27.4-alpine AS production

RUN apk add --no-cache gettext

COPY ./init-scripts/ /docker-entrypoint.d/
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /docker-entrypoint.d/100-init-project-env-variables.sh

COPY nginx/templates/nginx.conf.template /etc/nginx/templates/
COPY --from=builder /app/dist /usr/share/nginx/html

RUN chmod +x /docker-entrypoint.d/*.sh

RUN echo "nginx -s reload;" > /reload.sh && \
    chmod +x /reload.sh

# CMD ["sh", "-c", \
#     "envsubst '$$SERVER_NAME' < /etc/nginx/templates/nginx.conf.template \
#      > /etc/nginx/conf.d/app.conf && exec nginx -g 'daemon off;'"]


CMD ["sh", "-c", \
    "/docker-entrypoint.d/100-init-project-env-variables.sh && \
     envsubst '$$SERVER_NAME' < /etc/nginx/templates/nginx.conf.template \
     > /etc/nginx/conf.d/app.conf && \
     exec nginx -g 'daemon off;'"]
