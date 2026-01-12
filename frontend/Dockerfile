# ---------- Build Stage ----------
FROM node:20 AS build

WORKDIR /app

COPY package*.json ./

# Alle Dependencies installieren
RUN npm install

# Vite global installieren, nur für Build
RUN npm install -g vite

COPY . .

ARG VITE_API_URL
ENV VITE_API_URL=${VITE_API_URL}

# Build ausführen
RUN vite build

# ---------- Runtime Stage ----------
FROM nginx:alpine

COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
