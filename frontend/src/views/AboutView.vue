<template>
  <div class="about-view">
    <div class="about-view-card">
      <h2 class="about-view-title">Acerca de PDFAnalyzer</h2>
      <p class="about-view-desc">Esta aplicación permite analizar archivos PDF y visualizar sus metadatos, protección, formularios y firmas digitales.</p>
      <ul class="about-view-list">
        <li>Frontend desarrollado en <span>Vue.js</span> + <span>CSS puro</span></li>
        <li>Backend en <span>FastAPI</span></li>
        <li>Comunicación por <span>HTTP (JSON)</span></li>
      </ul>
      <p class="about-view-note">Consulta la documentación automática del backend en <a href="http://localhost:8000/docs" class="about-view-link">/docs</a></p>
    </div>
    <footer class="about-view-footer">Desarrollado con Vue.js &amp; CSS puro</footer>
  </div>
</template>

<script setup>
// No logic needed for AboutView
</script>

<style src="@/assets/aboutview.css"></style>
