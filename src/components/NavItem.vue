<script setup lang="ts">
const isExpanded = useState('isExpanded')

defineProps({
  dataItem: {
    type: Object,
    required: true
  }
})


</script>

<template>
  <NuxtLink :to="dataItem.path" class="h-12 flex items-center hover:bg-red-100 cursor-pointer">
    <li class="px-4 list-none flex gap-1 items-center">
      <Icon size="18" :name="dataItem.icon" />
      <span v-show="isExpanded">{{ dataItem.text }}</span>
    </li>
  </NuxtLink>
</template>