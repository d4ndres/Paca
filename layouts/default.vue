<script setup lang="ts">
import { ref, onMounted } from 'vue';

const isExpanded = ref(true);

const toggleWidth = () => {
  isExpanded.value = !isExpanded.value;
};

onMounted(() => {
  const handleResize = () => {
    isExpanded.value = window.innerWidth >= 768;
  };
  handleResize(); // Verificar el tamaño inicial de la ventana
  window.addEventListener('resize', handleResize); // Actualizar el valor de isExpanded cuando se cambie el tamaño de la ventana
});
</script>

<template>
  <div class="flex bg-slate-500 h-[100vh] ">
    <aside class="w-[300px] flex flex-col transition-all duration-300" :style="{ width: isExpanded ? '300px' : '0' }">
      <NuxtLink to="/dashboard" class="h-[40px] flex items-center px-2">Actualización digital</NuxtLink>
      <NuxtLink to="/dashboard/trabajadores" class="hover:bg-red-100 p-2 transition duration-300">Trabajadores</NuxtLink>
      <NuxtLink to="/dashboard/labores" class="hover:bg-red-100 p-2 transition duration-300">Labores</NuxtLink>
    </aside>
    <div class="w-full bg-green-50 ">
      <header class="bg-slate-400 h-[40px] flex items-center px-2">
        <div>
          <button @click="toggleWidth">Toggle Width</button>
        </div>
      </header>
      <main class="h-[calc(100vh-40px)] overflow-y-auto">
        <slot />
      </main>
    </div>
  </div>
</template>