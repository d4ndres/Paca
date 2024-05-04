<script setup lang="ts">
const route = useRoute();

onMounted(() => {  
  navigateToDefault();
});

watchEffect(() => {
  navigateToDefault();
});

function navigateToDefault() {
  if (route.name === 'home-actividades') {
    navigateTo('/home/actividades/registros');
  }
}

</script>


<template>
  <div class="p-4">
    <h2 class="text-2xl mb-4">Actividades Realizadas</h2>
    <NuxtPage></NuxtPage>
  </div>
</template>