<script setup lang="ts">
import { useActividades } from '~/store/pacaStore'
const store = useActividades()
const { actividadesToShow } : any = storeToRefs(store)


</script>

<template>
  <div class="mb-4">
    <NuxtLink class="rounded-md bg-pink-200 p-2" to="/home/actividades/nuevo_registro">
      Nuevo Registro
    </NuxtLink>
  </div>
  <DataTable :data="actividadesToShow" />
</template>