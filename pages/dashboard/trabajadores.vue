<script setup>

let headersList = {
  "Accept": "*/*",
  "User-Agent": "Thunder Client (https://www.thunderclient.com)",
  "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZjeHhhY3l3bXdzd3RtcnR1YXNkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTM4ODU2NjAsImV4cCI6MjAyOTQ2MTY2MH0.WrODjGbFW4HcPwpkTPdf6UWbJTLll8yiXcoagT59d1k"
}

const workers = ref([]);

onMounted( async () => {
  const data = await fetch('https://vcxxacywmwswtmrtuasd.supabase.co/rest/v1/trabajadores?select=*', {
    method: "GET",
    headers: headersList
  })

  workers.value = await data.json();
})

</script>

<template>
  <section class="p-2">
    <h2 class="text-2xl mb-4">Todos los trabajadores</h2>
    <table class="min-w-full bg-white border border-gray-300">
      <thead>
        <tr>
          <th class="px-6 py-3 border-b border-gray-300 text-left text-xs font-semibold uppercase tracking-wider">Nombre</th>
          <th class="px-6 py-3 border-b border-gray-300 text-left text-xs font-semibold uppercase tracking-wider">Especialidad</th>
          <!-- <th class="px-6 py-3 border-b border-gray-300 text-left text-xs font-semibold uppercase tracking-wider">Fecha de Creación</th> -->
        </tr>
      </thead>
      <tbody>
        <tr v-for="w in workers" :key="w.id" class="hover:bg-gray-100">
          <td class="px-6 py-4 whitespace-nowrap">{{ w.nombre }}</td>
          <td class="px-6 py-4 whitespace-nowrap">{{ w.especialidad }}</td>
          <!-- <td class="px-6 py-4 whitespace-nowrap">{{ w.created_at }}</td> -->
        </tr>
      </tbody>
    </table>
  </section>
</template>