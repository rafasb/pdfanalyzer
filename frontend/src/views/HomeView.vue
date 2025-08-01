<template>
  <div class="home-view">
    <div class="home-view-card">
      <h1 class="home-view-title">PDFAnalyzer</h1>
      <PdfUpload @upload-success="fetchAnalysis" />
      <div v-if="analysisLoading" class="analyze-feedback-loading">⏳ Analizando PDF...</div>
      <div v-if="analysisError" class="analyze-feedback-error">❌ {{ analysisError }}</div>
      <AnalyzeResult :result="analysisResult" />
    </div>
    <footer class="home-view-footer">Desarrollado con Vue.js &amp; CSS puro</footer>
  </div>
</template>

<script setup>

import { ref } from 'vue'
import axios from 'axios'
import PdfUpload from '@/components/PdfUpload.vue'
import AnalyzeResult from '@/components/AnalyzeResult.vue'

const analysisResult = ref(null)
const analysisError = ref('')
const analysisLoading = ref(false)

async function fetchAnalysis(file) {
  analysisError.value = ''
  analysisLoading.value = true
  analysisResult.value = null
  try {
    const formData = new FormData()
    formData.append('file', file)
    const response = await axios.post('http://localhost:8000/analyze', formData, {
      headers: { 'Content-Type': 'multipart/form-data' }
    })
    analysisResult.value = response.data
  } catch (err) {
    analysisError.value = err.response?.data?.detail || 'Error al analizar el archivo.'
    analysisResult.value = null
  } finally {
    analysisLoading.value = false
  }
}
</script>

<style src="@/assets/homeview.css"></style>
