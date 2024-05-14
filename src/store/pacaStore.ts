import {defineStore} from 'pinia'
import { ref, computed } from 'vue'


export const useActividades = defineStore('actividades', () => {
  const actividades = ref<any>([])
  
  const setActividades = (data: any) => {
    actividades.value = data
  }

  const addActividad = (data: any) => {
    actividades.value.push(data)
  }

  const actividadesToShow = computed(() => actividades.value.map( (actividad : any) => {
    return {
      id: actividad.id,
      fecha: actividad.fecha,
      empleado: actividad.Empleado.nombre,
      labor: actividad.labor,
      lote: actividad.lote
    }
  }))

  return {actividades, setActividades, addActividad, actividadesToShow}
})