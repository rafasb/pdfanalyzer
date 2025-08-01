<template>
  <div class="flex flex-col items-center justify-center min-h-[80vh] bg-gradient-to-br from-blue-50 to-blue-100">
    <div class="w-full max-w-xl bg-white rounded-xl shadow-lg p-8">
      <h2 class="text-3xl font-extrabold text-blue-700 mb-6 text-center drop-shadow">Acerca de PDFAnalyzer</h2>
      <p class="mb-4 text-gray-700 text-lg text-center">Esta aplicación permite analizar archivos PDF y visualizar sus metadatos, protección, formularios y firmas digitales.</p>
      <ul class="list-disc pl-6 mb-4 text-gray-600">
        <li>Frontend desarrollado en <span class="font-semibold text-blue-600">Vue.js</span> + <span class="font-semibold text-blue-600">Tailwind CSS</span></li>
        <li>Backend en <span class="font-semibold text-blue-600">FastAPI</span></li>
        <li>Comunicación por <span class="font-semibold text-blue-600">HTTP (JSON)</span></li>
      </ul>
      <p class="text-sm text-gray-500 text-center">Consulta la documentación automática del backend en <a href="http://localhost:8000/docs" class="text-blue-600 underline">/docs</a></p>
    </div>
    <footer class="mt-8 text-gray-400 text-sm text-center">Desarrollado con Vue.js & Tailwind CSS</footer>
  </div>
</template>

<script setup>
// No logic needed for AboutView
</script>
