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
  <section>
    
    <article v-if="inMain">
      <div>
        <NuxtLink to="/dashboard/labores/nuevo_registro">
          Nuevo Registro
        </NuxtLink>
      </div>

      <div>
        Lista de todos los registros
      </div>
    </article>

    <NuxtPage  />
  </section>
</template>