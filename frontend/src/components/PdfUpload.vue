<template>
  <div class="max-w-md mx-auto p-4 bg-white rounded shadow">
    <h2 class="text-lg font-bold mb-4">Subir PDF</h2>
    <form @submit.prevent="handleUpload">
      <input type="file" accept="application/pdf" @change="onFileChange" class="mb-2" />
      <button type="submit" class="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700" :disabled="!file">Subir</button>
    </form>
    <p v-if="error" class="text-red-500 mt-2">{{ error }}</p>
    <p v-if="success" class="text-green-600 mt-2">{{ success }}</p>
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
