import { serverSupabaseClient } from '#supabase/server'


// const { data, error } = await supabase
//   .from('TrabajadoresHorasExtra')
//   .insert([
//     { some_column: 'someValue' },
//     { some_column: 'otherValue' },
//   ])
//   .select()

export default defineEventHandler(async (event) => {
  const body = await readBody(event)
  const client = await serverSupabaseClient(event)
  const horasExtra = await client.from('TrabajadoresHorasExtra').insert( body ).select()
  return horasExtra

})
