# Fase 2: Desarrollo del backend - PDFAnalyzer

Este documento detalla el proceso recomendado para el desarrollo del backend de PDFAnalyzer. Sirve como guía flexible y puede adaptarse según necesidades del proyecto.

---

## 1. Configuración del entorno

- Crear un entorno virtual (`python -m venv venv`).
- Instalar dependencias desde `requirements.txt`:
  ```
  pip install -r backend/requirements.txt
  ```
- Dependencias necesarias:
  - fastapi
  - uvicorn
  - pymupdf
  - pikepdf
  - PyPDF2
  - httpx (para tests)
  - python-multipart (para subir archivos)


## 2. Estructura recomendada del proyecto

```
backend/
  ├── app/
  │   ├── main.py
  │   ├── api/
  │   ├── services/
  │   ├── models/
  │   └── utils/
  ├── tests/
  └── requirements.txt
```
- Separar rutas, lógica de negocio y utilidades para facilitar mantenimiento y escalabilidad.

## 3. Implementación de endpoints

- **/upload**: Recibe archivos PDF usando `UploadFile`.
- **/analyze**: Procesa el PDF y retorna resultados.
- Validar tipo y tamaño de archivo.
- Documentar endpoints usando OpenAPI (FastAPI lo genera automáticamente).

## 4. Integración de librerías de análisis PDF

- **PyMuPDF**: Extracción de metadatos y contenido.
- **pikepdf**: Detección de protección y cifrado.
- **PyPDF2**: Manipulación básica y formularios.
- Crear servicios independientes para cada tipo de análisis.

## 5. Lógica de extracción

- **Metadatos**: Autor, título, fecha, etc. (servicio independiente)
- **Protección**: ¿Está cifrado? ¿Requiere contraseña? (servicio independiente)
- **Formularios**: ¿Contiene campos interactivos? (servicio independiente)
- **Firmas**: ¿Incluye firmas digitales? (servicio independiente)
- Todos los servicios manejan excepciones y devuelven errores claros.

## 6. Pruebas unitarias y de integración

- Usar `pytest` para pruebas automáticas.
- Los tests de los endpoints `/upload` y `/analyze` están en `backend/tests/test_api_pdf.py`.
- El test de `/analyze` valida la respuesta completa: metadatos, protección, formularios y firmas digitales.
- Para ejecutar los tests correctamente:
  1. Instala todas las dependencias (ver sección de entorno).
  2. Ejecuta:
     ```
     PYTHONPATH=backend pytest backend/tests/test_api_pdf.py
     ```
- Si ves errores de módulos faltantes, revisa que estén en `requirements.txt` e instalados.

## 7. Consideraciones adicionales

- **Seguridad**: Limitar tamaño de archivos, sanitizar entradas.
- **Rendimiento**: Procesar archivos de forma eficiente.
- **Escalabilidad**: Preparar el backend para múltiples usuarios concurrentes.
- **Documentación**: Mantener documentación técnica actualizada.

---

Este documento es una guía flexible y puede adaptarse según los avances y necesidades del desarrollo.
