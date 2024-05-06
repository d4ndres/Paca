<script setup lang="ts">
const inventario = ref<any[]>([])

onMounted( async () => {
  const response = await $fetch('/api/combustiblesInventario') as any
  inventario.value = response.data.map(( c : any) => {
    return {
      ...c,
      unidad: 'gal'      
    }
  })
})

</script>

<template>
  <h2 class="text-xl mb-4">Inventario de Combustibles</h2>
  <DataTable :data="inventario" />
</template>