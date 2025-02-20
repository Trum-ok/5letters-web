# build
FROM node:20.18.3-alpine AS builder
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --silent
COPY . .
RUN npm run build

# prod
FROM nginx:1.27.4-alpine AS production
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/dist /usr/share/nginx/html

ARG VITE_BACK_PORT

RUN echo "nginx -s reload;" > /reload.sh && \
    chmod +x /reload.sh

CMD ["nginx", "-g", "daemon off;"]
