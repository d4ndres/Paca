<script setup lang="ts">
import { useEmpleadosStore } from '~/store/empleados';
const store = useEmpleadosStore();
const {empleados} = storeToRefs(store);

</script>

<template>
  <div class="p-4">
    <h2 class="text-2xl mb-4">Empleados</h2>
    <DataTable :data="empleados" />
  </div>
</template>