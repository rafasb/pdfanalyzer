import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import HomeView from '@/views/HomeView.vue'

describe('HomeView.vue', () => {
  it('renderiza el título principal', () => {
    const wrapper = mount(HomeView)
    expect(wrapper.text()).toContain('PDFAnalyzer')
  })

  it('incluye los componentes PdfUpload y AnalyzeResult', () => {
    const wrapper = mount(HomeView)
    expect(wrapper.findComponent({ name: 'PdfUpload' }).exists()).toBe(true)
    expect(wrapper.findComponent({ name: 'AnalyzeResult' }).exists()).toBe(true)
  })
})
