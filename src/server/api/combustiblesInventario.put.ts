import { serverSupabaseClient } from '#supabase/server'

export default defineEventHandler(async (event) => {
  const body = await readBody(event)
  const client = await serverSupabaseClient(event)
  const responeSupabase = await client
  .from('CombustibleInventario')
  .upsert({ id: body.id, cantidadActual: body.cantidadActual} as any)
  return responeSupabase
})
