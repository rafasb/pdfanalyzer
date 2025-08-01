# Estructura de directorios recomendada para PDFAnalyzer

```
pdfanalyzer/
├── backend/                # API y lógica de análisis PDF (FastAPI, Python)
│   ├── app/                # Código fuente principal del backend
│   │   ├── api/            # Rutas y controladores de la API
│   │   ├── services/       # Lógica de negocio y análisis PDF
│   │   ├── models/         # Modelos de datos y esquemas
│   │   ├── utils/          # Utilidades y helpers
│   │   └── main.py         # Punto de entrada de la aplicación FastAPI
│   ├── tests/              # Pruebas unitarias y de integración del backend
│   ├── requirements.txt    # Dependencias de Python
│   └── README.md           # Documentación específica del backend
│
├── frontend/               # Aplicación web (Vue + Tailwind)
│   ├── src/                # Código fuente principal del frontend
│   │   ├── components/     # Componentes Vue reutilizables
│   │   ├── views/          # Vistas principales de la app
│   │   ├── assets/         # Imágenes, estilos, fuentes, etc.
│   │   ├── router/         # Configuración de rutas
│   │   ├── store/          # Estado global (Vuex/Pinia)
│   │   └── App.vue         # Componente raíz
│   ├── public/             # Archivos estáticos públicos
│   ├── tests/              # Pruebas del frontend
│   ├── package.json        # Dependencias de Node.js
│   └── README.md           # Documentación específica del frontend
│
├── docs/                   # Documentación general y ejemplos de uso
│   └── arquitectura.md     # Descripción de la arquitectura del proyecto
│
├── .gitignore              # Exclusión de archivos para git
├── README.md               # Documentación principal del proyecto
└── LICENSE                 # Licencia del proyecto
```

Esta estructura facilita la escalabilidad, la colaboración y el mantenimiento, separando claramente el backend, frontend, documentación y pruebas.
