<script setup>
// No logic needed
</script>

<template>
  <div class="min-h-screen bg-gray-50">
    <nav class="bg-blue-700 text-white px-4 py-3 flex justify-between items-center">
      <div class="font-bold text-lg">PDFAnalyzer</div>
      <div class="space-x-4">
        <router-link to="/" class="hover:underline">Inicio</router-link>
        <router-link to="/about" class="hover:underline">Acerca de</router-link>
      </div>
    </nav>
    <router-view />
  </div>
</template>
<style scoped>
/* Puedes agregar estilos globales aquí si lo necesitas */
</style>
