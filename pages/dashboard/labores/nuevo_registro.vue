<script setup lang="ts">

const useAppScriptPostNewActivity = async (data: any) => {
  let headersList = {
    "Accept": "*/*",
    "Content-Type": "application/json"
  }

  let bodyContent = JSON.stringify(data);

  return await fetch("https://script.google.com/macros/s/AKfycbyxflabla-_wfYAu1IsiLgBMnKG3aOR7sK0UERdT8m1yqF6EauNCoOKMP8CXs_N_3Q/exec?nuevaActividad=true", {
    method: "POST",
    body: bodyContent,
    headers: headersList
  });
}

const sendInfo = (ev: Event) => {
  console.log(ev);
  useAppScriptPostNewActivity(ev)

  formData.value = {};
}


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
    <FormKit type="form" @submit="sendInfo" :actions="false" v-model="formData">
      <FormKit type="select" name="trabajador" label="Seleccione trabajador" :options="['Diego', 'Andrés', 'Maria']" />
      <FormKit type="date" name="fecha" label="Fecha" />
      <FormKit type="text" name="labor" label="Labor" />
      <FormKit type="number" name="lote" label="Lote" />
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
  </div>

</template>