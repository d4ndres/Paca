import { serverSupabaseClient } from '#supabase/server'

export default eventHandler(async (event) => {
  const body = await readBody(event)
  const client = await serverSupabaseClient(event)
  const responeSupabase = await client.from('EmpleadoActividadRealizada').insert( body ).select()
  return responeSupabase
})