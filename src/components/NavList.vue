<script setup lang="ts">
const isExpanded = useState('isExpanded')
const navList = [
  { path: '/home', text: 'Home', icon: 'ion:home-outline' },
  { path: '/home/empleados', text: 'Empleados', icon: 'fa6-regular:address-card' },
  { path: '/home/actividades', text: 'Actividades', icon: 'octicon:clippy' },
  { path: '/home/horasExtra', text: 'Horas extra', icon: 'fa6-regular:clock' }
]

</script>
<template>
  <aside class="w-[300px] bg-slate-500  flex flex-col transition-all duration-300" :style="{ width: isExpanded ? '300px' : '50px' }">
    <NavItem v-for="item in navList" :key="item.path" :dataItem="item" />
  </aside>
</template>