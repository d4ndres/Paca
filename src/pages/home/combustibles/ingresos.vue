<script setup lang="ts">
const session = useSupabaseSession()
const user_id = computed(() => session.value?.user.id)

type CombustibleInventario = {
  id: number,
  tipo: string,
  cantidadActual: number,
}

const combustibles = ref<CombustibleInventario[]>([])
const catalogoCombustibles = computed(() => {
  return [
    { label: 'seleccionar', value: null },
    ...combustibles.value.map(({ id, tipo }) => Object.assign({ value: id, label: tipo }))
  ]
})

onMounted(async () => {
  await getInventario()
})

const getInventario = async () => {
  const response = await $fetch('/api/combustiblesInventario') as { data: any[] }
  combustibles.value = response.data
}


const formData = ref<any>({})
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


const sendInfo = (fields: any) => {
  const { fecha, combustible_id, valorUnitario, cantidad } = fields
  $fetch('/api/combustiblesIngresos', {
    method: 'post',
    body: { fecha, combustible_id, valorUnitario, cantidad, user_id: user_id.value }
  }).then(({ error, data }) => {
    return new Promise((resolve, reject) => {
      if (error) reject(error)
      resolve(data)
    })
  }).then(async ([ingreso]: any) => {
    const { cantidadActual } = combustibles.value.find(({ id }) => id == ingreso.combustible_id) as CombustibleInventario
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
    .catch(() => {
      setStateSuccess(false)
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
  <h2 class="text-xl mb-4">Ingreso de combustible</h2>
  <div>
    <FormKit type="form" @submit="sendInfo" :actions="false" v-model="formData">
      <FormKit type="date" name="fecha" label="Fecha" />
      <FormKit type="select" name="combustible_id" label="Seleccione combustible" :options="catalogoCombustibles"
        validation="required" />
      <FormKit type="number" name="valorUnitario" label="valor unidad" />
      <FormKit type="number" name="cantidad" label="Cantidad" />
      <FormKit type="submit" label="Guardar" />
    </FormKit>
  </div>
</template>