<template>
  <div v-if="result" class="analyze-result">
    <h2 class="analyze-result-title">📊 Resultados del Análisis</h2>
    <div class="analyze-result-grid single-column">
      <div class="analyze-result-card analyze-result-card-meta">
        <h3 class="analyze-result-card-title">📋 Metadatos</h3>
        <pre class="analyze-result-meta">{{ JSON.stringify(result.metadata, null, 2) }}</pre>
      </div>
      <div class="analyze-result-card analyze-result-card-prot">
        <h3 class="analyze-result-card-title">🔒 Protección</h3>
        <pre>{{ JSON.stringify(result.protection, null, 2) }}</pre>
      </div>
      <div class="analyze-result-card analyze-result-card-form">
        <h3 class="analyze-result-card-title">📝 Formularios</h3>
        <pre>{{ JSON.stringify(result.forms, null, 2) }}</pre>
      </div>
      <div class="analyze-result-card analyze-result-card-sign">
        <h3 class="analyze-result-card-title">✍️ Firmas</h3>
        <pre>{{ JSON.stringify(result.signatures, null, 2) }}</pre>
      </div>
    </div>
  </div>
  <div v-else class="analyze-result-empty">
    <div class="analyze-result-empty-box">
      <p class="analyze-result-empty-title">📊 Los resultados del análisis aparecerán aquí</p>
      <p class="analyze-result-empty-desc">Sube un archivo PDF para comenzar</p>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue'
defineProps({
  result: {
    type: Object,
    default: null
  }
})
</script>

<style src="@/assets/analyzeresult.css"></style>
