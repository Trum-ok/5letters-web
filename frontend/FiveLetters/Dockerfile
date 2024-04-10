FROM node:18-alpine AS react-build
WORKDIR /app/FiveLetters
COPY package.json .
RUN npm install
COPY . .
RUN npm run build

FROM node:18-alpine AS react-prod
WORKDIR /app/FiveLetters

COPY --from=react-build /app/FiveLetters/dist /app/FiveLetters/dist

COPY package.json .
COPY vite.config.ts .

RUN npm install typescript
EXPOSE 3001

CMD ["npm", "run", "preview"]