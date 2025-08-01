<template>
  <div class="max-w-3xl mx-auto py-8">
    <h1 class="text-3xl font-bold text-blue-700 mb-6 text-center">PDFAnalyzer</h1>
    <PdfUpload @upload-success="fetchAnalysis" />
    <AnalyzeResult :result="analysisResult" />
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
