<script setup lang="ts">

definePageMeta({
  middleware: 'authenticated'
})
</script>

<template>
  <NuxtLayout>
    <NuxtPage></NuxtPage>
  </NuxtLayout>
</template>