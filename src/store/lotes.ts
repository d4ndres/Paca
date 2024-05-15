import {defineStore} from 'pinia'
import { ref, computed } from 'vue'


export const useLotes = defineStore('lotes', () => {
  const lotes = ref<any>([])
  
  const setLotes = (data: any) => {
    lotes.value = data
  }

  const lotesToSelect = computed(() => [
    { value: null, label: 'Seleccione un actividad' },
    ...lotes.value.map((combustible: any) => ({
      value: combustible.id,
      label: combustible.nombre
    }))
  ])

  return {lotes, setLotes, lotesToSelect}

})