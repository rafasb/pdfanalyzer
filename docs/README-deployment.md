# Guía de Despliegue - PDFAnalyzer

## Tabla de Contenidos
- [Requisitos del Sistema](#requisitos-del-sistema)
- [Despliegue con Docker](#despliegue-con-docker)
- [Despliegue Manual](#despliegue-manual)
- [Variables de Entorno](#variables-de-entorno)
- [Configuración de Producción](#configuración-de-producción)
- [Monitoreo y Logs](#monitoreo-y-logs)
- [Backup y Recuperación](#backup-y-recuperación)
- [Troubleshooting](#troubleshooting)

## Requisitos del Sistema

### Mínimos
- **CPU**: 2 cores
- **RAM**: 4GB
- **Almacenamiento**: 20GB disponibles
- **Sistema Operativo**: Linux Ubuntu 20.04+ / CentOS 7+ / Docker compatible

### Recomendados para Producción
- **CPU**: 4 cores
- **RAM**: 8GB
- **Almacenamiento**: 50GB SSD
- **Red**: Conexión estable a internet para dependencias

## Despliegue con Docker

### Docker Compose

```bash
# Clonar el repositorio
git clone https://github.com/rafasb/pdfanalyzer.git
cd pdfanalyzer

# Configurar variables de entorno
cp .env.example .env
nano .env

# Construir y ejecutar
docker-compose up -d --build
```

#### docker-compose.yml
```yaml
version: '3.8'

services:
  backend:
    build: ./backend
    container_name: pdfanalyzer-backend
    ports:
      - "8000:8000"
    environment:
      - ENVIRONMENT=production
      - MAX_FILE_SIZE_MB=50
      - CORS_ORIGINS=http://localhost:3000,https://yourdomain.com
    volumes:
      - ./uploads:/app/uploads
      - ./logs:/app/logs
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  frontend:
    build: ./frontend
    container_name: pdfanalyzer-frontend
    ports:
      - "3000:3000"
    environment:
      - VITE_API_URL=http://localhost:8000
      - NODE_ENV=production
    depends_on:
      - backend
    restart: unless-stopped

  nginx:
    image: nginx:alpine
    container_name: pdfanalyzer-nginx
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf
      - ./nginx/ssl:/etc/nginx/ssl
    depends_on:
      - frontend
      - backend
    restart: unless-stopped

volumes:
  uploads:
  logs:
```

## Despliegue Manual

### Backend (FastAPI)

```bash
# Prerrequisitos
sudo apt update
sudo apt install python3.11 python3.11-venv python3-pip

# Configuración del proyecto
cd backend
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Variables de entorno
cp .env.example .env
nano .env

# Ejecutar en producción
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Frontend (Vue.js)

```bash
# Prerrequisitos
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs

# Configuración del proyecto
cd frontend
npm install

# Build para producción
npm run build

# Servir con servidor web
sudo npm install -g serve
serve -s dist -l 3000
```


## Variables de Entorno

### Backend (.env)
```bash
# Entorno
ENVIRONMENT=production
DEBUG=false

# API Configuration
HOST=0.0.0.0
PORT=8000
WORKERS=4

# CORS
CORS_ORIGINS=https://yourdomain.com,https://www.yourdomain.com

# File Processing
MAX_FILE_SIZE_MB=50
UPLOAD_DIR=/app/uploads
TEMP_DIR=/app/temp

# Security
SECRET_KEY=your-super-secret-key-here
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# Logging
LOG_LEVEL=INFO
LOG_FILE=/app/logs/app.log

# Rate Limiting
RATE_LIMIT_PER_MINUTE=60
```

### Frontend (.env)
```bash
# API Configuration
VITE_API_URL=https://yourdomain.com/api
VITE_MAX_FILE_SIZE_MB=50

# Environment
NODE_ENV=production

# Analytics (opcional)
VITE_GA_TRACKING_ID=GA_MEASUREMENT_ID
```

## Configuración de Producción

### Systemd Services

#### Backend Service
```ini
# /etc/systemd/system/pdfanalyzer-backend.service
[Unit]
Description=PDFAnalyzer Backend API
After=network.target

[Service]
Type=exec
User=www-data
Group=www-data
WorkingDirectory=/opt/pdfanalyzer/backend
Environment=PATH=/opt/pdfanalyzer/backend/venv/bin
ExecStart=/opt/pdfanalyzer/backend/venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
```

#### Frontend Service
```ini
# /etc/systemd/system/pdfanalyzer-frontend.service
[Unit]
Description=PDFAnalyzer Frontend
After=network.target

[Service]
Type=exec
User=www-data
Group=www-data
WorkingDirectory=/opt/pdfanalyzer/frontend/dist
ExecStart=/usr/bin/serve -s . -l 3000
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
```

```bash
# Habilitar y iniciar servicios
sudo systemctl enable pdfanalyzer-backend pdfanalyzer-frontend
sudo systemctl start pdfanalyzer-backend pdfanalyzer-frontend
sudo systemctl status pdfanalyzer-backend pdfanalyzer-frontend
```

### SSL/TLS con Let's Encrypt

```bash
# Instalar Certbot
sudo apt install certbot python3-certbot-nginx

# Obtener certificado
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com

# Renovación automática
sudo crontab -e
# Añadir: 0 12 * * * /usr/bin/certbot renew --quiet
```

## Monitoreo y Logs

### Logs del Sistema
```bash
# Logs del backend
tail -f /app/logs/app.log

# Logs de Docker
docker-compose logs -f backend
docker-compose logs -f frontend

# Logs de Nginx
tail -f /var/log/nginx/pdfanalyzer_access.log
tail -f /var/log/nginx/pdfanalyzer_error.log

# Logs del sistema
journalctl -u pdfanalyzer-backend -f
journalctl -u pdfanalyzer-frontend -f
```

### Health Checks
```bash
# Backend health check
curl -f http://localhost:8000/health

# Frontend availability
curl -f http://localhost:3000

# Script de monitoreo básico
#!/bin/bash
# monitor.sh
if ! curl -f http://localhost:8000/health > /dev/null 2>&1; then
    echo "Backend is down!"
    # Reiniciar servicio o enviar alerta
fi
```

### Métricas con Prometheus (Opcional)
```yaml
# docker-compose.monitoring.yml
version: '3.8'
services:
  prometheus:
    image: prom/prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./monitoring/prometheus.yml:/etc/prometheus/prometheus.yml

  grafana:
    image: grafana/grafana
    ports:
      - "3001:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
```

## Backup y Recuperación

### Archivos a Respaldar
```bash
# Crear backup
backup_date=$(date +%Y%m%d_%H%M%S)
tar -czf pdfanalyzer_backup_$backup_date.tar.gz \
    --exclude='node_modules' \
    --exclude='venv' \
    --exclude='__pycache__' \
    /opt/pdfanalyzer

# Base de datos (si se añade en el futuro)
# pg_dump pdfanalyzer > pdfanalyzer_db_$backup_date.sql
```

### Script de Backup Automatizado
```bash
#!/bin/bash
# backup.sh
BACKUP_DIR="/backups"
DATE=$(date +%Y%m%d_%H%M%S)
RETENTION_DAYS=30

# Crear backup
tar -czf $BACKUP_DIR/pdfanalyzer_$DATE.tar.gz /opt/pdfanalyzer

# Limpiar backups antiguos
find $BACKUP_DIR -name "pdfanalyzer_*.tar.gz" -mtime +$RETENTION_DAYS -delete

# Cron job: 0 2 * * * /opt/scripts/backup.sh
```

## Troubleshooting

### Problemas Comunes

#### Backend no inicia
```bash
# Verificar logs
docker-compose logs backend

# Verificar puertos
netstat -tlnp | grep 8000

# Verificar permisos
ls -la /app/uploads
ls -la /app/logs
```

#### Frontend no carga
```bash
# Verificar build
npm run build

# Verificar variables de entorno
echo $VITE_API_URL

# Verificar conectividad con API
curl http://localhost:8000/health
```

#### Errores de CORS
```bash
# Verificar configuración CORS en backend
grep CORS_ORIGINS .env

# Verificar headers en respuesta
curl -I -X OPTIONS http://localhost:8000/upload
```

#### Uploads fallan
```bash
# Verificar permisos de directorio
chmod 755 uploads/
chown -R www-data:www-data uploads/

# Verificar límite de tamaño
grep MAX_FILE_SIZE .env
grep client_max_body_size /etc/nginx/sites-available/pdfanalyzer
```

### Comandos de Diagnóstico
```bash
# Estado de servicios
systemctl status pdfanalyzer-*

# Uso de recursos
htop
df -h
free -h

# Conectividad de red
netstat -tlnp
ss -tlnp

# Logs en tiempo real
tail -f /var/log/syslog | grep pdfanalyzer
```

### Contacto de Soporte
Para problemas específicos de despliegue:
- **Issues**: GitHub Issues del repositorio
- **Email**: rafasb@domain.com
- **Documentación**: `/docs/README-*.md`

---

*Última actualización: [Fecha]*
*Versión de la documentación: 1.0*
