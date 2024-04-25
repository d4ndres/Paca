export default defineNuxtRouteMiddleware((context) => {
  console.log('Authenticated middleware', context)
  const user = useSupabaseUser()
  if( !user.value ) {
    return navigateTo('/')
  }
})