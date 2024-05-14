<script setup lang="ts">
const isExpanded = useState('isExpanded')
const navList = [
  { path: '/home', text: 'Home', icon: 'home-outline' },
  { path: '/home/empleados', text: 'Empleados', icon: 'address-card' },
  { path: '/home/actividades', text: 'Actividades', icon: 'clippy' },
  { path: '/home/horasExtra', text: 'Horas extra', icon: 'clock' },
  { path: '/home/combustibles', text: 'Combustibles', icon: 'oil' }
]


const user = useSupabaseUser()
const username = computed(() => user.value?.user_metadata.email.split('@')[0])
const { auth } = useSupabaseClient()
const logout = async () => {
  const something = await auth.signOut()
  console.log('logout', something);
  return navigateTo('/')
}

</script>
<template>
  <aside class="w-[300px] bg-slate-500  flex flex-col justify-between transition-all duration-300"
    :style="{ width: isExpanded ? '300px' : '50px' }">
    <div>
      <NavItem v-for="item in navList" :key="item.path" :dataItem="item" />
    </div>
    <div class="">

      <!-- <button @click="logout" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-4 rounded">
        Cerrar sesión
      </button>
      <div class="flex justify-center items-center px-2">
        <span>{{ username }}</span>
        <Avatar />
      </div> -->

      <div class="h-12 flex items-center hover:bg-red-100 cursor-pointer">
        <li class="px-4 list-none flex gap-1 items-center">
          <Icon size="18" name="user" />
          <span v-show="isExpanded">{{ username }}</span>
        </li>
      </div>

      <div @click="logout" class="h-12 flex items-center hover:bg-red-100 cursor-pointer">
        <li class="px-4 list-none flex gap-1 items-center">
          <Icon size="18" name="logout" />
          <span v-show="isExpanded">Cerrar sesión</span>
        </li>
      </div>
    </div>
  </aside>
</template>