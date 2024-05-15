import {defineStore} from 'pinia'
import { ref, computed } from 'vue'


export const useVehiculos = defineStore('vehiculos', () => {
  const vehiculos = ref<any>([])
  
  const setVehiculos = (data: any) => {
    vehiculos.value = data
  }

  const vehiculosToSelect = computed(() => [
    { value: null, label: 'Seleccione un actividad' },
    ...vehiculos.value.map((combustible: any) => ({
      value: combustible.id,
      label: combustible.nombre
    }))
  ])

  return {vehiculos, setVehiculos, vehiculosToSelect}

})