<template>
  <div class="home-view">
    <div class="home-view-card">
      <h1 class="home-view-title">PDFAnalyzer</h1>
      <PdfUpload @upload-success="fetchAnalysis" />
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

async function fetchAnalysis(file) {
  try {
    const formData = new FormData()
    formData.append('file', file)
    const response = await axios.post('http://localhost:8000/analyze', formData, {
      headers: { 'Content-Type': 'multipart/form-data' }
    })
    analysisResult.value = response.data
  } catch (err) {
    analysisResult.value = null
  }
}
</script>

<style src="@/assets/homeview.css"></style>
