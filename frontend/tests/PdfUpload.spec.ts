import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import PdfUpload from '@/components/PdfUpload.vue'

// Nueva función para validar archivos
function validarArchivo(file) {
  if (!file) return 'No se ha seleccionado archivo.'
  if (file.type !== 'application/pdf') return 'Solo se permiten archivos PDF.'
  if (file.size > 10 * 1024 * 1024) return 'El archivo supera el tamaño máximo permitido (10MB).'
  if (!file.name.toLowerCase().endsWith('.pdf')) return 'El archivo debe tener extensión .pdf.'
  return ''
}

describe('PdfUpload.vue', () => {
  it('muestra el título y el botón correctamente', () => {
    const wrapper = mount(PdfUpload)
    expect(wrapper.find('.pdf-upload-title').text()).toContain('Subir PDF para Análisis')
    expect(wrapper.find('button.pdf-upload-btn').exists()).toBe(true)
  })

  it('valida tipo de archivo y muestra error si no es PDF', () => {
    const file = new File([''], 'test.txt', { type: 'text/plain' })
    expect(validarArchivo(file)).toContain('Solo se permiten archivos PDF.')
  })

  it('valida tamaño máximo y extensión', () => {
    const bigFile = new File([new ArrayBuffer(11 * 1024 * 1024)], 'big.pdf', { type: 'application/pdf' })
    expect(validarArchivo(bigFile)).toContain('El archivo supera el tamaño máximo permitido')

    const wrongExt = new File([''], 'archivo.txt', { type: 'application/pdf' })
    expect(validarArchivo(wrongExt)).toContain('El archivo debe tener extensión .pdf.')
  })
})
