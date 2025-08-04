# Dockerfile para el Frontend

# Usar una imagen base de Node.js
FROM node:20-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos necesarios al contenedor
COPY package.json package.json
COPY package-lock.json package-lock.json
COPY . /app

# Instalar las dependencias
RUN npm install


# Construir la aplicación para producción usando la variable VITE_API_URL
ARG VITE_API_URL=http://172.29.132.20:8000
ENV VITE_API_URL=$VITE_API_URL
RUN npm run build

# Exponer el puerto en el que se ejecutará el servidor
EXPOSE 3000

# Comando para ejecutar el servidor de producción
CMD ["npm", "start"]
