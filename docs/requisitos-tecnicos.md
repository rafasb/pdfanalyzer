# Requisitos técnicos de PDFAnalyzer

1. El backend debe estar desarrollado en Python utilizando FastAPI.
2. El análisis de PDFs debe realizarse con PyMuPDF (fitz) y, si es necesario, pikepdf o PyPDF2.
3. El frontend debe estar desarrollado con Vue y utilizar Tailwind CSS para el diseño.
4. La comunicación entre frontend y backend debe realizarse mediante API REST.
5. El sistema debe implementar pruebas unitarias y de integración tanto en backend como en frontend.
6. El límite de tamaño para archivos PDF subidos debe ser configurable (por defecto, 100 MB).
7. El sistema debe validar y sanitizar los archivos subidos para evitar riesgos de seguridad.
8. El despliegue debe realizarse obligatoriamente mediante Docker y Docker Compose, en entornos Linux.
9. El código debe estar organizado siguiendo la estructura de carpetas recomendada y buenas prácticas de desarrollo.
10. El sistema debe ser extensible para permitir la integración de nuevos módulos de análisis.
