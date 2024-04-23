<script setup lang="ts">

const workers = [
  "Ernesto Gutiérrez operador_1",
  "Carlos Guzman operador_2",
  "Carlos Armado Llanos operador_3",
  "Jose auxiliar_1",
  "Omar Fabian auxiliar_2",
  "no definido auxiliar_3",
  "Rafael Alvis bodeguero"
];
const lotes = Array.from({ length: 10 }, (_, index) => index);


const sendInfo = async (ev:any) => {
  console.log({
    "nombre_trabajador": ev.trabajador,
    "fecha": ev.fecha,
    "labor": ev.labor,
    "lote": ev.lote,
  });
  
  let headersList = {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.com)",
    "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZjeHhhY3l3bXdzd3RtcnR1YXNkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTM4ODU2NjAsImV4cCI6MjAyOTQ2MTY2MH0.WrODjGbFW4HcPwpkTPdf6UWbJTLll8yiXcoagT59d1k",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZjeHhhY3l3bXdzd3RtcnR1YXNkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTM4ODU2NjAsImV4cCI6MjAyOTQ2MTY2MH0.WrODjGbFW4HcPwpkTPdf6UWbJTLll8yiXcoagT59d1k",
    "Content-Type": "application/json"
  }

  let bodyContent = JSON.stringify({
    "nombre_trabajador": ev.trabajador,
    "fecha": ev.fecha,
    "labor": ev.labor,
    "lote": ev.lote,
  });

  let response = await fetch("https://vcxxacywmwswtmrtuasd.supabase.co/rest/v1/AvtividadesRealizadas?select=*", {
    method: "POST",
    body: bodyContent,
    headers: headersList
  });

  if( response.ok ) {
    isSuccess.value = true;
    setTimeout(() => {
      isSuccess.value = false;
    }, 3000);
  }
  
  formData.value = {};
}

const isSuccess = ref(false)
const formData = ref<any>({});
const hasHorasExtrasAntes = computed(() => {
  return formData.value.horasExtrasAntes;
})
const hasHorasExtrasDespues = computed(() => {
  return formData.value.horasExtrasDespues;
})

</script>

<template>
  <div>
    <div>
      <h3 class="text-2xl">Nuevo registro</h3>
    </div>
    <div class="flex justify-between">
      <FormKit type="form" @submit="sendInfo" :actions="false" v-model="formData">
        <FormKit type="select" name="trabajador" label="Seleccione trabajador" :options="workers" validation="required"/>
        <FormKit type="date" name="fecha" label="Fecha" />
        <FormKit type="text" name="labor" label="Labor" />
        <FormKit type="select" name="lote" label="Lote" :options="lotes" />
        <FormKit type="checkbox" name="horasExtrasAntes" label="Horas extras antes de la jornada" :value="false" />
        <div v-if="hasHorasExtrasAntes">
          <FormKit type="time" name="horaInicioAntes" label="Hora de inicio" />
          <FormKit type="time" name="horaFinalAntes" label="Hora final" />
        </div>
        <FormKit type="checkbox" name="horasExtrasDespues" label="Horas extras después de la jornada" :value="false" />
        <div v-if="hasHorasExtrasDespues">
          <FormKit type="time" name="horaInicioDespues" label="Hora de inicio" />
          <FormKit type="time" name="horaFinalDespues" label="Hora final" />
        </div>
        <FormKit type="submit" label="Guardar registro" />
      </FormKit>
      <div>
        <div v-if="isSuccess" class="alert alert-success" style="margin-top: 20px; padding: 10px; background-color: #d4edda; color: #155724; border-color: #c3e6cb; border-radius: 4px;">
          La entrega de información ha sido exitosa.
        </div>
      </div>
    </div>
  </div>
  

</template>