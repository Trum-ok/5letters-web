FROM node:16-alpine AS react-build
WORKDIR /app
COPY ./package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM python:3.11.1-alpine
WORKDIR /app
COPY --from=react-build /app/build ./build
COPY ./requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python", "app.py"]