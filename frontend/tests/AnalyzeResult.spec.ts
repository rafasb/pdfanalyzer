import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import AnalyzeResult from '@/components/AnalyzeResult.vue'

const mockResult = {
  metadata: { author: 'Autor', title: 'Título', page_count: 2 },
  protection: { encrypted: false },
  forms: { has_forms: false },
  signatures: { has_signatures: false }
}

describe('AnalyzeResult.vue', () => {
  it('muestra los resultados cuando hay datos', () => {
    const wrapper = mount(AnalyzeResult, { props: { result: mockResult } })
    expect(wrapper.text()).toContain('Resultados del Análisis')
    expect(wrapper.text()).toContain('Autor')
    expect(wrapper.text()).toContain('Protección')
    expect(wrapper.text()).toContain('Formularios')
    expect(wrapper.text()).toContain('Firmas')
  })

  it('muestra mensaje vacío si no hay resultado', () => {
    const wrapper = mount(AnalyzeResult, { props: { result: null } })
    expect(wrapper.text()).toContain('Los resultados del análisis aparecerán aquí')
  })
})
