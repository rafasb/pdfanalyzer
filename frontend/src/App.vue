<script setup>
// No logic needed
</script>

<template>
  <div>
    <nav class="app-nav">
      <div class="app-title">PDFAnalyzer</div>
      <div class="app-links">
        <router-link to="/" class="app-link">Inicio</router-link>
        <router-link to="/about" class="app-link">Acerca de</router-link>
      </div>
    </nav>
    <main class="app-main">
      <div class="app-content">
        <router-view />
      </div>
    </main>
  </div>
</template>
<style scoped>
/* Estilos en src/assets/app.css */
</style>
