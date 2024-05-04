<script setup lang="ts">
type ActividadesRealizadas = {
  id: number;
  created_at: string;
  nombre_trabajador: string;
  fecha: string;
  labor: string;
  lote: string;
};

const responseActividades = await $fetch('/api/actividades') as { AvtividadesRealizadas: ActividadesRealizadas[] };
console.log(responseActividades);

</script>

<template>
  <div class="mb-4">
    <NuxtLink class="rounded-md bg-pink-200 p-2" to="/home/actividades/nuevo_registro">
      Nuevo Registro
    </NuxtLink>
  </div>
  <!-- <DataTable :data="responseActividades" /> -->
</template>