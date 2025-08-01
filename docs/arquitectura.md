# Arquitectura de PDFAnalyzer

PDFAnalyzer está compuesto por dos grandes módulos: backend y frontend, comunicados mediante una API REST.

## Componentes principales

- **Frontend (Vue + CSS puro):**
  - Interfaz web para carga de PDFs y visualización de resultados.
  - Comunicación con el backend mediante peticiones HTTP.
  - Presentación clara y estructurada de los análisis.

- **Backend (FastAPI, Python):**
  - API REST para recibir archivos PDF y devolver resultados de análisis.
  - Procesamiento y análisis técnico de PDFs usando PyMuPDF, pikepdf y PyPDF2.
  - Validación, sanitización y gestión temporal de archivos.
  - Generación de informes descargables.

- **Despliegue:**
  - Contenedores Docker para backend y frontend.
  - Orquestación con Docker Compose.

## Flujo básico
1. El usuario accede a la web y sube un PDF.
2. El frontend envía el archivo al backend vía API REST.
3. El backend analiza el PDF y devuelve los resultados.
4. El frontend muestra los resultados y permite descargar el informe.

## Seguridad y buenas prácticas
- Los archivos PDF no se almacenan de forma permanente.
- Validación y sanitización de archivos subidos.
- Pruebas unitarias y de integración en ambos módulos.

---

Este documento puede ampliarse con diagramas y detalles técnicos según avance el desarrollo.
