import {defineStore} from 'pinia'
import { ref, computed } from 'vue'

export const useEmpleadosStore = defineStore('empleados', () => {
  const empleados = ref<any>([])

  const setEmpleados = (data: any) => {
    empleados.value = data
  }

  const empleadosToSelect = computed(() => [
    { value: null, label: 'Seleccione un empleado' },
    ...empleados.value.map((empleado: any) => ({
      value: empleado.id,
      label: empleado.nombre
    }))
  ])

  return { empleados, setEmpleados, empleadosToSelect }
})