<script lang="ts" setup>

const client = useSupabaseClient()



type user = {
  email: string
  password: string
}

const errorMessage = ref("")

const onSubmit = async ( { email, password} : user ) => {

  try {
    const { data, error } = await client.auth.signUp({ email, password })
  
    if ( error?.message ) {
      throw error
    } else {
      console.log(data);
      navigateTo('/')
    }
  } catch ( error : any ) {
    console.error(error.message)
    errorMessage.value = error.message
  }
}

</script>

<template>
  <div class="h-[100vh] w-full bg-lime-100 flex justify-center items-center">
    <div class="w-[300px] min-h-[350px] bg-white p-4 pt-0 flex flex-col shadow-xl">
      <div class="relative py-1 text-sm">
        <NuxtLink to="/login">
          volver
        </NuxtLink>
      </div>
      <div class="text-center flex-grow flex justify-center items-center flex-col min-h-[5rem]">
        <p>
          Actualización digital
        </p>
      </div>
      <FormKit type="form" :actions="false" @submit="onSubmit" >
        <FormKit label="Nombre de usuario" name="email" type="email" validation="required" />
        <FormKit label="Contraseña" name="password" type="password" validation="required" />
        <FormKit type="submit">Iniciar sección</FormKit>
      </FormKit>
      <!-- <NuxtLink to="/dashboard">dashboard</NuxtLink> -->
    </div>
  </div>
</template>