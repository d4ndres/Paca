<script setup lang="ts">
const isExpanded = useState('isExpanded', () => false)




onMounted(() => {
  const handleResize = () => {
    isExpanded.value = window.innerWidth >= 768;
  };
  handleResize();
  window.addEventListener('resize', handleResize); // Actualizar el valor de isExpanded cuando se cambie el tamaño de la ventana
});



</script>

<template>
  <div class="flex h-[100vh] ">
    <NavList />
    <div class="w-full ">
      <HeaderDasboard />
      <main class="h-[calc(100vh-40px)] overflow-y-auto">
        <slot />
      </main>
    </div>
  </div>
</template>