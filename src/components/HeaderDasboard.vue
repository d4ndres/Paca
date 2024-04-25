<script setup lang="ts">
const user = useSupabaseUser()
const username = computed(() => user.value?.user_metadata.email.split('@')[0])
const isExpanded = useState('isExpanded', () => false)

const toggleWidth = () => {
  isExpanded.value = !isExpanded.value;
};

const { auth } = useSupabaseClient()

const logout = async () => {
  const something =  await auth.signOut()
  console.log('logout', something);
  
  return navigateTo('/')
}


</script>

<template>
  <header class="bg-slate-400 h-9 flex justify-between items-center">
    <div @click="toggleWidth" class="w-9 hover:bg-red-100 h-full flex items-center justify-center cursor-pointer">
      <Icon v-show="isExpanded" size="24" name="gravity-ui:arrow-shape-left-to-line" />
      <Icon v-show="!isExpanded" size="24" name="gravity-ui:arrow-shape-right-to-line" />
    </div>

    <div class="mr-auto">
      <BreadCrumb />
    </div>

    <div class="flex gap-2">

      <button @click="logout" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-4 rounded">
        Cerrar sesión
      </button>
      <div class="flex justify-center items-center px-2">
        <span>{{ username }}</span>
        <Avatar />
      </div>
    </div>
  </header>
</template>

