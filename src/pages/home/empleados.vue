<script setup lang="ts">

type Trabajador = {
  id: number;
  created_at: string;
  nombre: string;
  especialidad: string;
};

const {trabajadores} = await $fetch('/api/empleados') as {trabajadores: Trabajador[]};
console.log(trabajadores);
</script>

<template>
  <div class="p-4">
    <h2 class="text-2xl mb-4">Empleados</h2>
    <DataTable :data="trabajadores" />
  </div>
</template>