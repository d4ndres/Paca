import { serverSupabaseClient } from '#supabase/server'

export default eventHandler(async (event) => {
  const client = await serverSupabaseClient(event)
  const responseSupabase = await client.from('Lote').select('*')
  return responseSupabase
})