FROM node:20-bookworm
WORKDIR /app
COPY package*.json ./
RUN npm ci || npm install
COPY . .
ENV NUXT_HOST=0.0.0.0
EXPOSE 3000
CMD ["npm","run","dev"]