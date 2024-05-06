<script setup lang="ts">
const isExpanded = useState('isExpanded')
const navList = [
  { path: '/home', text: 'Home', icon: 'home-outline' },
  { path: '/home/empleados', text: 'Empleados', icon: 'address-card' },
  { path: '/home/actividades', text: 'Actividades', icon: 'clippy' },
  { path: '/home/horasExtra', text: 'Horas extra', icon: 'clock' }
]

</script>
<template>
  <aside class="w-[300px] bg-slate-500  flex flex-col transition-all duration-300" :style="{ width: isExpanded ? '300px' : '50px' }">
    <NavItem v-for="item in navList" :key="item.path" :dataItem="item" />
  </aside>
</template>