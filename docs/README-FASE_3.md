# Fase 3: Desarrollo del frontend - PDFAnalyzer

Este documento guía el desarrollo del frontend y la integración con el backend.

## Resumen de arquitectura
- Frontend en Vue.js
- Backend en FastAPI (API REST en `/upload` y `/analyze`)
- Comunicación por HTTP (JSON)

## Checklist de tareas principales
- [ ] Inicializar proyecto Vue y configurar Tailwind CSS
- [ ] Crear componentes para carga de archivos y visualización de resultados
- [ ] Implementar comunicación con la API backend (`/upload`, `/analyze`)
- [ ] Desarrollar vistas principales y navegación
- [ ] Añadir validaciones y feedback al usuario
- [ ] Implementar pruebas de componentes y vistas

## Recomendaciones para el desarrollo
- Mantener la estructura modular en `src/components` y `src/views`
- Usar `axios` para llamadas HTTP
- Validar archivos antes de enviarlos al backend (tipo, tamaño)
- Mostrar mensajes claros de error y éxito
- Aprovechar la documentación automática del backend (`/docs`)

## Comandos útiles
- Instalar dependencias:
  ```
  npm install
  ```
- Ejecutar el frontend en desarrollo:
  ```
  npm run dev
  ```
- Ejecutar el backend:
  ```
  uvicorn app.main:app --reload --port 8000
  ```

## Siguientes pasos
- Avanza siguiendo el checklist y actualiza este documento conforme completes tareas.
- Documenta cualquier decisión relevante para facilitar el trabajo en equipo.
