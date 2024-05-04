<script setup lang="ts">

const responseTrabajadores = await $fetch('/api/empleados') as { trabajadores: Trabajador[] };
const trabajadores = computed(() => {
  const trabajadores = [{
    label: 'Seleccione trabajador',
    value: null
  }]
  return [
    ...trabajadores,
    ...responseTrabajadores.trabajadores.map((trabajador: Trabajador) => ({
      label: trabajador.nombre,
      value: trabajador.id
    }))
  ]
});


const isSuccess = ref(false)

const formData = ref<any>({});
const hasHorasExtrasAntes = computed(() => formData.value.horasExtrasAntes )
const hasHorasExtrasDespues = computed(() =>  formData.value.horasExtrasDespues )

const sendInfo = async (fields: any) => {
  const responseActividades = await $fetch('/api/actividades', {
    method: 'post',
    body: {
      trabajadorId: fields.trabajador,
      fecha: fields.fecha,
      labor: fields.labor,
      lote: fields.lote
    }
  });
  console.log(responseActividades);



  console.log(fields);
  return null

  const laborRealizada = {
    nombre_trabajador: fields.nombre_trabajador,
    fecha: fields.fecha,
    labor: fields.labor,
    lote: Number(fields.lote)
  }

  const horasExtras = []
  if (fields.horasExtrasAntes) {
    horasExtras.push({
      fecha: fields.fecha,
      nombre_trabajador: fields.nombre_trabajador,
      labor: fields.labor,
      lote: Number(fields.lote),
      horaInicio: fields.horaInicioAntes,
      horaDeSalida: fields.horaFinalAntes
    })
  }
  if (fields.horasExtrasDespues) {
    horasExtras.push({
      fecha: fields.fecha,
      nombre_trabajador: fields.nombre_trabajador,
      labor: fields.labor,
      lote: Number(fields.lote),
      horaInicio: fields.horaInicioDespues,
      horaDeSalida: fields.horaFinalDespues
    })
  }

  // const responseActividades = await $fetch('/api/actividades', {
  //   method: 'post',
  //   body: laborRealizada
  // });
  // console.log(responseActividades);


  if (fields.horasExtrasAntes || fields.horasExtrasDespues) {
    console.log(horasExtras);

    const responseHorasExtra: any = await $fetch('/api/horasExtra', {
      method: 'post',
      body: horasExtras
    });
    console.log(responseHorasExtra);

  }


}


</script>

<template>
  <div>
    <div>
      <h3 class="text-2xl">Nuevo registro</h3>
    </div>
    <div class="flex justify-between">
      <FormKit type="form" @submit="sendInfo" :actions="false" v-model="formData">
        <FormKit type="select" name="trabajador" label="Seleccione trabajador" :options="trabajadores" validation="required" />
        <FormKit type="date" name="fecha" label="Fecha" validation="required" />
        <FormKit type="text" name="labor" label="Labor" validation="required" />
        <FormKit type="number" name="lote" label="Lote" validation="required|min:0|max:10" />
        <FormKit type="checkbox" name="horasExtrasAntes" label="Horas extras antes de la jornada" :value="false" />
        <div v-if="hasHorasExtrasAntes">
          <FormKit type="time" name="horaInicioAntes" label="Hora de inicio" validation="required" />
          <FormKit type="time" name="horaFinalAntes" label="Hora final" validation="required" />
        </div>
        <FormKit type="checkbox" name="horasExtrasDespues" label="Horas extras después de la jornada" :value="false" />
        <div v-if="hasHorasExtrasDespues">
          <FormKit type="time" name="horaInicioDespues" label="Hora de inicio" validation="required" />
          <FormKit type="time" name="horaFinalDespues" label="Hora final" validation="required" />
        </div>
        <FormKit type="submit" label="Guardar registro" />
      </FormKit>
      <div>
        <div v-if="isSuccess" class="alert alert-success"
          style="margin-top: 20px; padding: 10px; background-color: #d4edda; color: #155724; border-color: #c3e6cb; border-radius: 4px;">
          La entrega de información ha sido exitosa.
        </div>
      </div>
    </div>
  </div>
</template>