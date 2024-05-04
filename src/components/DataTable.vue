<script setup lang="ts">
import { defineProps, computed } from 'vue';

const props = defineProps({
  data: {
    type: Array as () => Array<object>,
    required: true
  }
});

const headers = computed(() => {
  // Extract the keys from the first object in the data array
  return Object.keys(props.data[0]);
});

const rows = computed(() => {
  // Return the data array excluding the first object (header row)
  return props.data.slice(1);
});
</script>


<template>

  <table class="min-w-full bg-white border border-gray-300">
    <thead>
      <tr>
        <!-- Generate table header dynamically -->
        <th class="px-6 py-3 border-b border-gray-300 text-left text-xs font-semibold uppercase tracking-wider" v-for="(header, index) in headers" :key="index" >{{ header }}</th>
      </tr>
    </thead>
    <tbody>
      <!-- Generate table rows dynamically -->
      <tr v-for="(row, index) in rows" :key="index" class="hover:bg-gray-100">
        <td v-for="(value, key) in row" :key="key" class="px-6 py-4 whitespace-nowrap">{{ value }}</td>
      </tr>
    </tbody>
  </table>

</template>
