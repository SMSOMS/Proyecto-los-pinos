FROM node:22-alpine AS builder

# Declarar los argumentos de compilación (Build Args) para Astro
ARG PUBLIC_CHATBOT_WEBHOOK_URL
ARG PUBLIC_CHATBOT_TOKEN

# Asignar los argumentos a variables de entorno para que estén disponibles durante la compilación
ENV PUBLIC_CHATBOT_WEBHOOK_URL=$PUBLIC_CHATBOT_WEBHOOK_URL
ENV PUBLIC_CHATBOT_TOKEN=$PUBLIC_CHATBOT_TOKEN

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
