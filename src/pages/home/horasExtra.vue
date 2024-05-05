<script setup lang="ts">
const { error, data } = await $fetch('/api/empleadosHorasExtra') as any
const horasExtras = computed(() => data.map((horaExtra: any) => ({
  id: horaExtra.id,
  empleado: horaExtra.Empleado.nombre,
  labor: horaExtra.EmpleadoActividadRealizada.labor,
  lote: horaExtra.EmpleadoActividadRealizada.lote,
  fecha: horaExtra.EmpleadoActividadRealizada.fecha,
  horaInicio: horaExtra.horaInicio,
  horaSalida: horaExtra.horaSalida
})))
</script>

<template>
  <div class="p-4">
    <h2 class="text-2xl mb-4">Horas extra</h2>
    <DataTable :data="horasExtras" />
  </div>
</template>