<script setup lang="ts">
const route = useRoute()
const inMain = ref(isInMain())
watch(() => route.path, (newPath) => {
  inMain.value = newPath === '/dashboard/labores';
});

function isInMain() {
  return route.path === '/dashboard/labores' ? true : false
}



</script>

<template>
  <section class="p-2">
    
    <article v-if="inMain">
      <h2 class="text-2xl mb-4">Labores realizadas</h2>

      <div>
        <NuxtLink class="rounded-md bg-pink-200 p-2" to="/dashboard/labores/nuevo_registro">
          Nuevo Registro
        </NuxtLink>
      </div>

      <div>
        <!-- Lista de todos los registros -->
      </div>
    </article>

    <NuxtPage  />
  </section>
</template>