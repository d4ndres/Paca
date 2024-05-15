<script setup lang="ts">
const route = useRoute()
const inCombustibles = computed(() => route.name == 'home-combustibles' )


import { useCombustibles } from '~/store/combustibles';
import { useLotes } from '~/store/lotes';
import { useActividades } from '~/store/actividades';
import { useVehiculos } from '~/store/vehiculos';

const storeCombustibles = useCombustibles()
const storeLotes = useLotes()
const storeActividades = useActividades()
const storeVehiculos = useVehiculos()

onMounted(() => {
  $fetch('/api/combustiblesInventario').then(({ data }) => { storeCombustibles.setCombustibles(data) })
  $fetch('/api/actividades').then(({ data }) => { storeActividades.setActividades(data) })
  $fetch('/api/vehiculos').then(({ data }) => { storeVehiculos.setVehiculos(data) })
  $fetch('/api/lotes').then(({ data }) => { storeLotes.setLotes(data) })
})
</script> 

<template>
  <NuxtLayout name="content">
    <h2 class="text-2xl mb-4">Combustibles</h2>
    <div class="flex gap-4" v-if="inCombustibles">
      <NuxtLink class="bg-white shadow-lg rounded-lg p-4 w-64 hover:bg-red-100" to="/home/combustibles/inventario">Inventario</NuxtLink>
      <NuxtLink class="bg-white shadow-lg rounded-lg p-4 w-64 hover:bg-red-100" to="/home/combustibles/ingresos">Ingresos</NuxtLink>
      <NuxtLink class="bg-white shadow-lg rounded-lg p-4 w-64 hover:bg-red-100" to="/home/combustibles/salida">Salida</NuxtLink>
    </div>
    <NuxtPage />
  </NuxtLayout>
</template>