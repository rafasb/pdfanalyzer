# Dockerfile para el Frontend

# Usar una imagen base de Node.js
FROM node:20-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos necesarios al contenedor
COPY frontend/package.json package.json
COPY frontend/package-lock.json package-lock.json
COPY frontend/ /app

# Instalar las dependencias
RUN npm install

# Construir la aplicación para producción
RUN npm run build

# Exponer el puerto en el que se ejecutará el servidor
EXPOSE 3000

# Comando para ejecutar el servidor de producción
CMD ["npm", "start"]
