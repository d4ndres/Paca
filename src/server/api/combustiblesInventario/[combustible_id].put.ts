import { serverSupabaseClient } from '#supabase/server'

export default defineEventHandler(async (event) => {
  const body = await readBody(event)
  const id = Number(getRouterParam(event, 'combustible_id'))

  const client = await serverSupabaseClient(event)
  const responeSupabase = await client
  .from('CombustibleInventario')
  .update({ cantidadActual: body.nuevaCantidad } as never)
  .eq('id', id )
  return responeSupabase
})
