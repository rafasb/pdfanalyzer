<template>
  <div class="flex flex-col items-center justify-center min-h-[80vh] bg-gradient-to-br from-blue-50 to-blue-100">
    <div class="w-full max-w-2xl bg-white rounded-xl shadow-lg p-8">
      <h1 class="text-4xl font-extrabold text-blue-700 mb-8 text-center drop-shadow">PDFAnalyzer</h1>
      <PdfUpload @upload-success="fetchAnalysis" />
      <AnalyzeResult :result="analysisResult" />
    </div>
    <footer class="mt-8 text-gray-400 text-sm text-center">Desarrollado con Vue.js & Tailwind CSS</footer>
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
