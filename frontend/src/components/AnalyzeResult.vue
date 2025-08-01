<template>
  <div v-if="result" class="max-w-2xl mx-auto p-4 bg-white rounded shadow mt-6">
    <h2 class="text-lg font-bold mb-4">Resultados del Análisis</h2>
    <div class="space-y-2">
      <div>
        <span class="font-semibold">Nombre:</span> {{ result.filename }}
      </div>
      <div>
        <span class="font-semibold">Metadatos:</span>
        <pre class="bg-gray-100 p-2 rounded text-xs">{{ result.metadata }}</pre>
      </div>
      <div>
        <span class="font-semibold">Protección:</span> {{ result.protection }}
      </div>
      <div>
        <span class="font-semibold">Formularios:</span> {{ result.forms }}
      </div>
      <div>
        <span class="font-semibold">Firmas:</span> {{ result.signatures }}
      </div>
    </div>
  </div>
  <div v-else class="max-w-2xl mx-auto p-4 text-gray-500">No hay resultados para mostrar.</div>
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
