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

const analysisResult = ref(null)

async function fetchAnalysis(filename) {
  try {
    const response = await axios.post('http://localhost:8000/analyze', { filename })
    analysisResult.value = response.data
  } catch (err) {
    analysisResult.value = null
  }
}
</script>

<style src="@/assets/homeview.css"></style>
