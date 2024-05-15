<script setup lang="ts">
import { useCombustibles } from '~/store/combustibles';
const storeCombustibles = useCombustibles()
import { useLotes } from '~/store/lotes';
import { useActividades } from '~/store/actividades';
import { useVehiculos } from '~/store/vehiculos';
import { useEmpleadosStore } from '~/store/empleados';

const { vehiculosToSelect } = storeToRefs(useVehiculos())
const { empleadosToSelect } = storeToRefs(useEmpleadosStore())
const { actividadesToSelect } = storeToRefs(useActividades())
const { lotesToSelect } = storeToRefs(useLotes())
const { combustiblesToSelect, combustibles } = storeToRefs(useCombustibles())

function dateNow() {
    const fechaActual = new Date();
    const año = fechaActual.getFullYear();
    const mes = String(fechaActual.getMonth() + 1).padStart(2, '0');const dia = String(fechaActual.getDate()).padStart(2, '0');
    return `${año}-${mes}-${dia}`;
}

const session = useSupabaseSession()
const user_id = computed(() => session.value?.user.id)

const formData = ref<any>({});
const isSuccess = ref<null | boolean>(null)

function setStateSuccess(state: boolean) {
  isSuccess.value = state
  if (state) {
    formData.value = {}
  }

  setTimeout(() => {
    isSuccess.value = null
  }, 3000)
}

const sendInfo = async ( fields: any ) => {
  const bodyGastos = {
    ...fields,
    user_id: user_id.value
  }


  $fetch('/api/combustiblesGastos', {
    method: 'post',
    body: bodyGastos
  })
  .then(({ error, data }) => {
    return new Promise((resolve, reject) => {
      if (error) reject(error)
      resolve(data)
    })
  })
  .then(async ([gastosSaved] : any) => {
    const bodyHistorial = {
      fecha: fields.fecha,
      cantidad: -fields.cantidadDeCombustibleDepositada,
      combustible_id: fields.combustible_id,
      user_id: user_id.value,
      gasto_id: gastosSaved.id
    }
    
    const response = await $fetch('/api/combustiblesHistorial', {
      method: 'post',
      body: bodyHistorial
    })

    return new Promise( (resolve, reject ) => {
      if( response.error ) reject(response.error)
      resolve(response.data)
    })
  })
  .then(async ([ingreso]: any) => {
    const { cantidadActual } = combustibles.value.find(({ id } : any) => id == ingreso.combustible_id) as any
    const nuevaCantidad = cantidadActual + ingreso.cantidad

    const response = await $fetch(`/api/combustiblesInventario/${ingreso.combustible_id}`, {
      method: 'put',
      body: { nuevaCantidad }
    })

    if (response?.status == 204) {
      setStateSuccess(true)

    } else {
      setStateSuccess(false)
    }

  })  
  .catch( error => {
    setStateSuccess(false)
  })
  .finally( () => {
    $fetch('/api/combustiblesInventario').then(({ data }) => { storeCombustibles.setCombustibles(data) })
  })
}

</script>

<template>
    <Teleport to="body">
    <div v-if="isSuccess === true" class="fixed bottom-0 right-0 p-4 bg-green-500 text-white shadow-lg rounded-lg">
      La entrega de información ha sido exitosa.
    </div>
    <div v-if="isSuccess === false" class="fixed bottom-0 right-0 p-4 bg-red-500 text-white shadow-lg rounded-lg">
      Ha ocurrido un error en la entrega de información.
    </div>
  </Teleport>
  <FormKit type="form" @submit="sendInfo" :actions="false" v-model="formData">
    <FormKit :value="dateNow()" type="date" name="fecha" label="Fecha" validation="required" />
    <FormKit type="select" name="vehiculo_id" label="Vehículo" :options="vehiculosToSelect" validation="required" />
    <FormKit type="select" name="empleado_id" label="Empleado" :options="empleadosToSelect" validation="required" />
    <FormKit type="select" name="actividad_id" label="Actividad" :options="actividadesToSelect" validation="required" />
    <FormKit type="select" name="lote_id" label="Lote" :options="lotesToSelect" validation="required" /> 
    <FormKit type="select" name="combustible_id" label="Tipo de combustible" :options="combustiblesToSelect" validation="required" />
    <FormKit type="number" name="cantidadDeCombustibleDepositada" label="Cantidad de combustible depositada" validation="required" />
    <FormKit type="submit" label="Guardar registro" />
  </FormKit>
</template>