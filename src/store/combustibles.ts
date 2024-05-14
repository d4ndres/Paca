import {defineStore} from 'pinia'
import { ref, computed } from 'vue'


export const useCombustibles = defineStore('combustibles', () => {
  const combustibles = ref<any>([])
  
  const setCombustibles = (data: any) => {
    combustibles.value = data
  }

  const combustiblesToSelect = computed(() => [
    { value: null, label: 'Seleccione un combustible' },
    ...combustibles.value.map((combustible: any) => ({
      value: combustible.id,
      label: combustible.tipo
    }))
  ])

  return {combustibles, setCombustibles, combustiblesToSelect}

})