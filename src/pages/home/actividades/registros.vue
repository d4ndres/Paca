<script setup lang="ts">

const responseActividades = ref({
  error: null,
  data: []
})

onMounted( async () => {
  responseActividades.value = await $fetch('/api/actividades') as any
})

const actividades = computed(() => {
  if( responseActividades.value.data.length ) {
    return responseActividades.value.data.map( (actividad: any) => ({
      id: actividad.id,
      fecha: actividad.fecha,
      empleado: actividad.Empleado.nombre,
      labor: actividad.labor,
      lote: actividad.lote
    }))
  }
  return []
})

</script>

<template>
  <div class="mb-4">
    <NuxtLink class="rounded-md bg-pink-200 p-2" to="/home/actividades/nuevo_registro">
      Nuevo Registro
    </NuxtLink>
  </div>
  <DataTable :data="actividades" />
</template>