<script setup lang="ts">

const responseTrabajadores = await $fetch('/api/empleados') as { trabajadores: empleado[] };
const trabajadores = computed(() => {
  const trabajadores = [{
    label: 'Seleccione trabajador',
    value: null
  }]
  return [
    ...trabajadores,
    ...responseTrabajadores.trabajadores.map((trabajador: empleado) => ({
      label: trabajador.nombre,
      value: trabajador.id
    }))
  ]
});


const isSuccess = ref<boolean|null>(null)

const formData = ref<any>({});
const hasHorasExtrasAntes = computed(() => formData.value.horasExtrasAntes )
const hasHorasExtrasDespues = computed(() =>  formData.value.horasExtrasDespues )

const sendInfo = async ( fields: any ) => {

  const { empleado_id, fecha, labor, lote} = fields
  $fetch('/api/actividades', {
    method: 'post',
    body: { empleado_id, fecha, labor, lote}
  }).then( ({ error, data }) => {
    return new Promise( (resolve, reject) => {
      if (error) reject(error)
      resolve(data)
    }) 
  }).then( async ( [actividad] : any) => {
    
    const horasExtras = []

    if( fields.horasExtrasAntes ) {
      horasExtras.push({
        empleado_id,
        actividadRealizada_id: actividad.id,
        horaInicio: fields.horaInicioAntes,
        horaSalida: fields.horaFinalAntes
      })
    }

    if( fields.horasExtrasDespues ) {
      horasExtras.push({
        empleado_id,
        actividadRealizada_id: actividad.id,
        horaInicio: fields.horaInicioDespues,
        horaSalida: fields.horaFinalDespues
      })
    }

    if( horasExtras.length ) {
      const { error, data } = await $fetch('/api/empleadosHorasExtra', {
        method: 'post',
        body: horasExtras
      })

      if( !error ) {
        setStateSuccess(true)
      }

    } else {
      setStateSuccess(true)
      
    }
  }).catch( error => {
    console.log(error);
    isSuccess.value = false
  }) 
}

function setStateSuccess( state : boolean  ) {
  isSuccess.value = state
  if( state ) {
    formData.value = {}
  }

  setTimeout( () => {
    isSuccess.value = null
  }, 3000)
}


</script>

<template>
  <div>
    <div>
      <h3 class="text-2xl">Nuevo registro</h3>
    </div>
    <div class="flex justify-between">
      <FormKit type="form" @submit="sendInfo" :actions="false" v-model="formData">
        <div>
          <FormKit type="select" name="empleado_id" label="Seleccione trabajador" :options="trabajadores" validation="required" />
          <FormKit type="date" name="fecha" label="Fecha" validation="required" />
          <FormKit type="text" name="labor" label="Labor" validation="required" />
          <FormKit type="number" name="lote" label="Lote" validation="required|min:0|max:10" />
        </div>
        
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
      <Teleport to="body">
        <div v-if="isSuccess === true" class="fixed bottom-0 right-0 p-4 bg-green-500 text-white shadow-lg rounded-lg">
          La entrega de información ha sido exitosa.
        </div>
        <div v-if="isSuccess === false" class="fixed bottom-0 right-0 p-4 bg-red-500 text-white shadow-lg rounded-lg">
          Ha ocurrido un error en la entrega de información.
        </div>
      </Teleport>
    </div>
  </div>
</template>
