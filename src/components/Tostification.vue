<script>
defineProps({
  isSuccess: Boolean
})
</script>

<template>
  <Teleport>
    <div class="fixed top-0 right-0 p-4 bg-green-500 text-white shadow-lg rounded-lg" v-if="isSuccess">
      <p>Registro exitoso</p>
    </div>
    <div class="fixed top-0 right-0 p-4 bg-red-500 text-white shadow-lg rounded-lg" v-if="isSuccess === false">
      <p>Error en el registro</p>
    </div>
  </Teleport>
</template>