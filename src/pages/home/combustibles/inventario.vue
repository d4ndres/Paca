<script setup lang="ts">
import { useCombustibles } from '~/store/combustibles';
const store = useCombustibles()
const { combustibles } = storeToRefs(store)
</script>

<template>
  <h2 class="text-xl mb-4">Inventario de Combustibles</h2>
  <DataTable :data="combustibles" />
</template>