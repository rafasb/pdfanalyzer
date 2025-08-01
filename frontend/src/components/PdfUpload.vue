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
        :disabled="!file"
      >
        🚀 Subir y Analizar PDF
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
import axios from 'axios'
import { defineEmits } from 'vue'

const file = ref(null)
const error = ref('')
const success = ref('')
const emit = defineEmits(['upload-success'])

function onFileChange(e) {
  error.value = ''
  success.value = ''
  const selected = e.target.files[0]
  if (!selected) return
  if (selected.type !== 'application/pdf') {
    error.value = 'Solo se permiten archivos PDF.'
    file.value = null
    return
  }
  file.value = selected
}

async function handleUpload() {
  if (!file.value) return
  const formData = new FormData()
  formData.append('file', file.value)
  try {
    const response = await axios.post('http://localhost:8000/upload', formData, {
      headers: { 'Content-Type': 'multipart/form-data' }
    })
    success.value = 'Archivo subido correctamente.'
    error.value = ''
    emit('upload-success', file.value)
  } catch (err) {
    error.value = err.response?.data?.detail || 'Error al subir el archivo.'
    success.value = ''
  }
}
</script>

<style src="@/assets/pdfupload.css"></style>
