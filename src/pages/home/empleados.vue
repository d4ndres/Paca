<script setup lang="ts">



const {trabajadores} = await $fetch('/api/empleados') as {trabajadores: empleado[]};
</script>

<template>
  <div class="p-4">
    <h2 class="text-2xl mb-4">Empleados</h2>
    <DataTable :data="trabajadores" />
  </div>
</template>