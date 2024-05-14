<script setup lang="ts">

const isExpanded = useState('isExpanded', () => false)
const toggleWidth = () => {
  isExpanded.value = !isExpanded.value;
};




</script>

<template>
  <header class="bg-slate-400 h-9 flex justify-between items-center">
    <div @click="toggleWidth" class="w-9 hover:bg-red-100 h-full flex items-center justify-center cursor-pointer">
      <Icon v-show="isExpanded" size="24" name="arrow-shape-left-to-line" />
      <Icon v-show="!isExpanded" size="24" name="arrow-shape-right-to-line" />
    </div>

    <div class="mr-auto">
      <BreadCrumb />
    </div>

  </header>
</template>

