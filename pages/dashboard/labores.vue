<script setup>


let headersList = {
  "Accept": "*/*",
  "User-Agent": "Thunder Client (https://www.thunderclient.com)",
  "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZjeHhhY3l3bXdzd3RtcnR1YXNkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTM4ODU2NjAsImV4cCI6MjAyOTQ2MTY2MH0.WrODjGbFW4HcPwpkTPdf6UWbJTLll8yiXcoagT59d1k"
}

const actividadesRealizadas = ref([]);

const consultarActividades = async () => {
  const data = await fetch('https://vcxxacywmwswtmrtuasd.supabase.co/rest/v1/AvtividadesRealizadas?select=*', {
    method: "GET",
    headers: headersList
  })
  actividadesRealizadas.value = await data.json();
}

onMounted(async () => {
  await consultarActividades();
})

onUpdated(async () => {
  await consultarActividades();
})



const route = useRoute()
const inMain = ref(isInMain())
watch(() => route.path, (newPath) => {
  inMain.value = newPath === '/dashboard/labores';
});

function isInMain() {
  return route.path === '/dashboard/labores' ? true : false
}



</script>

<template>
  <section class="p-2">

    <article v-if="inMain">
      <h2 class="text-2xl mb-4">Labores realizadas</h2>

      <div class="mb-4">
        <NuxtLink class="rounded-md bg-pink-200 p-2" to="/dashboard/labores/nuevo_registro">
          Nuevo Registro
        </NuxtLink>
      </div>

      <div>
        <table class="min-w-full bg-white border border-gray-300">
          <thead>
            <tr>
              <th class="px-6 py-3 border-b border-gray-300 text-left text-xs font-semibold uppercase tracking-wider">
                Lote
              </th>
              <th class="px-6 py-3 border-b border-gray-300 text-left text-xs font-semibold uppercase tracking-wider">
                Labor
              </th>
              <th class="px-6 py-3 border-b border-gray-300 text-left text-xs font-semibold uppercase tracking-wider">
                Nombre del trabajador
              </th>
              <th class="px-6 py-3 border-b border-gray-300 text-left text-xs font-semibold uppercase tracking-wider">
                Fecha
              </th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="w in actividadesRealizadas" :key="w.id" class="hover:bg-gray-100">
              <td class="px-6 py-4 whitespace-nowrap">{{ w.lote }}</td>
              <td class="px-6 py-4 whitespace-nowrap">{{ w.labor }}</td>
              <td class="px-6 py-4 whitespace-nowrap">{{ w.nombre_trabajador }}</td>
              <td class="px-6 py-4 whitespace-nowrap">{{ w.fecha }}</td>

            </tr>
          </tbody>
        </table>
      </div>
    </article>

    <NuxtPage />
  </section>
</template>