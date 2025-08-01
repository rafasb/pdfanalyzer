<template>
  <div class="max-w-2xl mx-auto py-8">
    <h2 class="text-2xl font-bold text-blue-700 mb-4">Acerca de PDFAnalyzer</h2>
    <div class="bg-white rounded shadow p-6">
      <p class="mb-2">Esta aplicación permite analizar archivos PDF y visualizar sus metadatos, protección, formularios y firmas digitales.</p>
      <ul class="list-disc pl-6 mb-2">
        <li>Frontend desarrollado en Vue.js + Tailwind CSS</li>
        <li>Backend en FastAPI</li>
        <li>Comunicación por HTTP (JSON)</li>
      </ul>
      <p class="text-sm text-gray-500">Consulta la documentación automática del backend en <a href="http://localhost:8000/docs" class="text-blue-600 underline">/docs</a></p>
    </div>
  </div>
</template>

<script setup>
// No logic needed for AboutView
</script>
