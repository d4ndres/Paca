<script lang="ts" setup>
definePageMeta({
  middleware: 'unauthenticated'
})


type user = {
  email: string
  password: string
}

const { auth } = useSupabaseClient()

const signIn = async ( ev : user ) => {
  try {
    const { error } = await auth.signInWithPassword(ev)
    if( error ) {
      throw error
    } else {
      navigateTo('/home')
    }
  } catch ( error : any ) {
    console.error(error.message)
  }
}

</script>

<template>
  <div class="h-[100vh] w-full bg-lime-100 flex justify-center items-center">
    <div class="w-[300px] min-h-[350px] bg-white p-4 pt-0 flex flex-col shadow-xl">
      <div class="text-center flex-grow flex justify-center items-center flex-col min-h-[5rem]">
        <span>
          Actualización digital
        </span>
      </div>
      <FormKit type="form" :actions="false" @submit="signIn">
        <FormKit label="Nombre de usuario" name="email" type="email" validation="required" />
        <FormKit label="Contraseña" name="password" type="password" validation="required" />
        <FormKit type="submit">Iniciar sección</FormKit>
      </FormKit>
    </div>
  </div>
</template>