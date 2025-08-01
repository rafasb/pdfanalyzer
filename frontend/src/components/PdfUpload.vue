<template>
  <div class="mb-8">
    <h2 class="text-2xl font-bold text-gray-800 mb-6 text-center">Subir PDF para Análisis</h2>
    <form @submit.prevent="handleUpload" class="space-y-4">
      <div class="relative">
        <input 
          type="file" 
          accept="application/pdf" 
          @change="onFileChange" 
          class="w-full p-4 border-2 border-dashed border-blue-300 rounded-lg hover:border-blue-400 focus:border-blue-500 focus:outline-none transition-colors cursor-pointer"
          :class="{ 'border-red-300': error, 'border-green-300': success }"
        />
        <div class="absolute inset-0 flex items-center justify-center pointer-events-none text-gray-500">
          <span v-if="!file">📄 Selecciona un archivo PDF</span>
          <span v-else class="text-blue-600 font-medium">{{ file.name }}</span>
        </div>
      </div>
      <button 
        type="submit" 
        class="w-full bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 disabled:bg-gray-300 disabled:cursor-not-allowed transition-colors font-medium"
        :disabled="!file"
      >
        🚀 Subir y Analizar PDF
      </button>
    </form>
    <div v-if="error" class="mt-4 p-3 bg-red-50 border border-red-200 rounded-lg">
      <p class="text-red-700 text-sm">❌ {{ error }}</p>
    </div>
    <div v-if="success" class="mt-4 p-3 bg-green-50 border border-green-200 rounded-lg">
      <p class="text-green-700 text-sm">✅ {{ success }}</p>
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
    emit('upload-success', file.value.name)
  } catch (err) {
    error.value = err.response?.data?.detail || 'Error al subir el archivo.'
    success.value = ''
  }
}
</script>
