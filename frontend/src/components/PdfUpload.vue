<template>
  <div class="pdf-upload">
    <h2 class="pdf-upload-title">Subir PDF para Análisis</h2>
    <form @submit.prevent="handleUpload" class="pdf-upload-form">
      <div class="pdf-upload-input-wrapper">
        <input 
          type="file" 
          accept="application/pdf" 
          @change="onFileChange" 
          class="pdf-upload-input"
        />
        <div class="pdf-upload-input-label">
          <span v-if="!file">📄 Selecciona un archivo PDF</span>
          <span v-else class="pdf-upload-filename">{{ file.name }}</span>
        </div>
      </div>
      <button 
        type="submit" 
        class="pdf-upload-btn"
        :disabled="!file || loading"
      >
        <span v-if="loading">⏳ Procesando...</span>
        <span v-else>🚀 Subir y Analizar PDF</span>
      </button>
    </form>
    <div v-if="error" class="pdf-upload-error">
      <p>❌ {{ error }}</p>
    </div>
    <div v-if="success" class="pdf-upload-success">
      <p>✅ {{ success }}</p>
    </div>
  </div>
</template>

<script setup>

import { ref } from 'vue'
const file = ref(null)
const error = ref('')
const success = ref('')
const loading = ref(false)
const emit = defineEmits(['upload-success'])

function onFileChange(e) {
  error.value = ''
  success.value = ''
  const selected = e.target.files[0]
  if (!selected) return
  // Validación tipo
  if (selected.type !== 'application/pdf') {
    error.value = 'Solo se permiten archivos PDF.'
    file.value = null
    return
  }
  // Validación tamaño (máx 10MB)
  if (selected.size > 10 * 1024 * 1024) {
    error.value = 'El archivo supera el tamaño máximo permitido (10MB).'
    file.value = null
    return
  }
  // Validación nombre
  if (!selected.name.toLowerCase().endsWith('.pdf')) {
    error.value = 'El archivo debe tener extensión .pdf.'
    file.value = null
    return
  }
  file.value = selected
}

async function handleUpload() {
  if (!file.value) return
  error.value = ''
  success.value = ''
  emit('upload-success', file.value)
}
// El feedback de éxito/error se muestra en el análisis
</script>

<style src="@/assets/pdfupload.css"></style>
