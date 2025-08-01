<template>
  <div v-if="result" class="mt-8">
    <h2 class="text-2xl font-bold text-gray-800 mb-6 text-center">📊 Resultados del Análisis</h2>
    <div class="grid gap-4">
      <div class="bg-blue-50 border border-blue-200 rounded-lg p-4">
        <h3 class="font-bold text-blue-700 mb-2">📄 Archivo</h3>
        <p class="text-gray-700">{{ result.filename }}</p>
      </div>
      <div class="bg-gray-50 border border-gray-200 rounded-lg p-4">
        <h3 class="font-bold text-gray-700 mb-2">📋 Metadatos</h3>
        <pre class="bg-white p-3 rounded border text-xs text-gray-600 overflow-auto max-h-32">{{ JSON.stringify(result.metadata, null, 2) }}</pre>
      </div>
      <div class="bg-yellow-50 border border-yellow-200 rounded-lg p-4">
        <h3 class="font-bold text-yellow-700 mb-2">🔒 Protección</h3>
        <p class="text-gray-700">{{ result.protection }}</p>
      </div>
      <div class="bg-green-50 border border-green-200 rounded-lg p-4">
        <h3 class="font-bold text-green-700 mb-2">📝 Formularios</h3>
        <p class="text-gray-700">{{ result.forms }}</p>
      </div>
      <div class="bg-purple-50 border border-purple-200 rounded-lg p-4">
        <h3 class="font-bold text-purple-700 mb-2">✍️ Firmas</h3>
        <p class="text-gray-700">{{ result.signatures }}</p>
      </div>
    </div>
  </div>
  <div v-else class="mt-8 text-center">
    <div class="bg-gray-50 border-2 border-dashed border-gray-300 rounded-lg p-8">
      <p class="text-gray-500 text-lg">📊 Los resultados del análisis aparecerán aquí</p>
      <p class="text-gray-400 text-sm mt-2">Sube un archivo PDF para comenzar</p>
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
