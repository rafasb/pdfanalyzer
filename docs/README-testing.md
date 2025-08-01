# Estrategia de Testing para PDFAnalyzer

## Objetivo

Establecer una estrategia de testing integral que garantice la calidad del código en cada fase del desarrollo, implementando pruebas unitarias y de integración tanto en el backend como en el frontend.

## Estructura de Pruebas

```
pdfanalyzer/
├── backend/
│   └── tests/
│       ├── unit/
│       │   ├── test_pdf_services.py
│       │   ├── test_models.py
│       │   └── test_utils.py
│       ├── integration/
│       │   ├── test_api_endpoints.py
│       │   ├── test_file_processing.py
│       │   └── test_report_generation.py
│       └── fixtures/
│           └── sample_pdfs/
└── frontend/
    └── tests/
        ├── unit/
        │   ├── components/
        │   ├── stores/
        │   └── utils/
        ├── integration/
        └── fixtures/
```

## Herramientas de Testing

### Backend
- **pytest**: Framework principal de testing
- **pytest-asyncio**: Para pruebas asíncronas con FastAPI
- **httpx**: Cliente HTTP para pruebas de API
- **pytest-cov**: Cobertura de código

### Frontend
- **Vitest**: Framework de testing para Vue 3
- **@vue/test-utils**: Utilidades para testing de componentes Vue
- **jsdom**: Entorno DOM para pruebas

## Tipos de Pruebas por Componente

### Backend - Pruebas Unitarias
- **Servicios de análisis PDF**: Validar extracción de metadatos, detección de protección, formularios y firmas
- **Modelos de datos**: Verificar serialización/deserialización de esquemas
- **Utilidades**: Funciones de validación, sanitización y helpers

### Backend - Pruebas de Integración
- **Endpoints de la API**: Probar flujo completo de carga y análisis
- **Procesamiento de archivos**: Validar manejo de diferentes tipos de PDF
- **Generación de informes**: Verificar creación de reportes descargables

### Frontend - Pruebas Unitarias
- **Componentes**: Renderizado, props, eventos y estados
- **Store/Estado**: Mutaciones, acciones y getters
- **Utilidades**: Funciones de formateo, validación y helpers

### Frontend - Pruebas de Integración
- **Flujo completo**: Carga de archivo → análisis → visualización de resultados
- **Comunicación con API**: Manejo de respuestas exitosas y errores
- **Navegación**: Rutas y transiciones entre vistas

## Comandos de Testing

### Backend
```bash
# Ejecutar todas las pruebas
pytest

# Ejecutar pruebas con cobertura
pytest --cov=app --cov-report=html

# Ejecutar solo pruebas unitarias
pytest tests/unit/

# Ejecutar solo pruebas de integración
pytest tests/integration/

# Ejecutar pruebas en modo verbose
pytest -v

# Ejecutar pruebas específicas
pytest tests/unit/test_pdf_services.py::test_extract_metadata
```

### Frontend
```bash
# Ejecutar todas las pruebas
npm run test

# Ejecutar pruebas con cobertura
npm run test:coverage

# Ejecutar pruebas en modo watch
npm run test:watch

# Ejecutar pruebas específicas
npm run test -- --grep "FileUpload"

# Ejecutar pruebas de integración
npm run test:integration
```

## Criterios de Calidad

### Cobertura Mínima
- **Backend**: 85% de cobertura de código
- **Frontend**: 80% de cobertura de componentes y utilidades críticas

### Casos de Prueba Obligatorios
- ✅ Análisis de PDFs protegidos, formularios y con firmas
- ✅ Manejo de archivos corruptos o inválidos
- ✅ Validación de límites de tamaño de archivo
- ✅ Respuestas de error de la API
- ✅ Estados de carga y feedback al usuario

## Integración en el Flujo de Desarrollo

### Pre-commit
- Ejecutar pruebas unitarias automáticamente antes de cada commit
- Verificar que no se rompe la funcionalidad existente

### CI/CD
- Ejecutar suite completa de pruebas en cada pull request
- Bloquear merge si las pruebas fallan o la cobertura es insuficiente
- Generar reportes de cobertura automáticamente

## Desarrollo por Fases

| Fase | Descripción | Tipo de Pruebas |
|------|-------------|-----------------|
| **Fase 2** (Backend) | Implementar pruebas unitarias para cada servicio desarrollado | Unitarias |
| **Fase 3** (Frontend) | Crear pruebas para cada componente y vista | Unitarias + Integración |
| **Fase 4** (Integración) | Añadir pruebas end-to-end del flujo completo | E2E |
| **Fase 5** (Despliegue) | Validar pruebas en entorno de producción | Smoke Tests |

## Buenas Prácticas

- 📝 **Escribir pruebas antes o durante el desarrollo** (TDD/BDD)
- 🏷️ **Usar nombres descriptivos** para las pruebas
- 🎯 **Mantener pruebas simples** y enfocadas en un solo aspecto
- 🔧 **Utilizar fixtures y mocks** para datos de prueba
- 📚 **Documentar casos de prueba complejos**
- 🔄 **Revisar y actualizar pruebas** regularmente

## Configuración de Herramientas

### pytest.ini
```ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --strict-markers --strict-config
markers =
    slow: marks tests as slow
    integration: marks tests as integration tests
    unit: marks tests as unit tests
```

### vitest.config.js
```javascript
import { defineConfig } from 'vitest/config'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  test: {
    environment: 'jsdom',
    coverage: {
      reporter: ['text', 'html'],
      threshold: {
        global: {
          branches: 80,
          functions: 80,
          lines: 80,
          statements: 80
        }
      }
    }
  }
})
```