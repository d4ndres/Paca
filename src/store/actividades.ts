import {defineStore} from 'pinia'
import { ref, computed } from 'vue'


export const useActividades = defineStore('actividades', () => {
  const actividades = ref<any>([])
  
  const setActividades = (data: any) => {
    actividades.value = data
  }

  const actividadesToSelect = computed(() => [
    { value: null, label: 'Seleccione un actividad' },
    ...actividades.value.map((actividad: any) => ({
      value: actividad.id,
      label: actividad.nombre
    }))
  ])

  return {actividades, setActividades, actividadesToSelect}

})