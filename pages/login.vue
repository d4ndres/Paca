<script lang="ts" setup>


type user = {
  username: string
  password: string
}

// const router = useRouter()
// const userLoggedIn = useState<user|null>()

const onSubmit = ( fields : user ) => {
  // userLoggedIn.value = { 
  //   username: fields.username,
  //   password: fields.password
  // }

  // localStorage.setItem('user', JSON.stringify(userLoggedIn.value))

  // router.push('/dashboard')
}

</script>

<template>
  <div class="h-[100vh] w-full bg-lime-100 flex justify-center items-center">
    <div class="w-[300px] h-[350px] bg-white p-4 flex flex-col shadow-xl">
      <div class="text-center flex-grow flex justify-center items-center">
        Actualización digital
      </div>
      <FormKit type="form" :actions="false" @submit="onSubmit">
        <FormKit label="Nombre de usuario" name="username" type="text" validation="required" />
        <FormKit label="Contraseña" name="password" type="password" validation="required" />
        <FormKit type="submit">Iniciar sección</FormKit>
      </FormKit>
      <!-- <NuxtLink to="/dashboard">dashboard</NuxtLink> -->
    </div>
  </div>
</template>