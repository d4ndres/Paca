<script setup lang="ts">

definePageMeta({
  middleware: 'authenticated'
})

import { useEmpleadosStore } from '~/store/empleados'
const store = useEmpleadosStore()

onMounted( () => {
  $fetch('/api/empleados')
  .then( ({trabajadores}) => {
    store.setEmpleados(trabajadores)
  })
})


</script>

<template>
  <NuxtLayout>
    <NuxtPage></NuxtPage>
  </NuxtLayout>
</template>