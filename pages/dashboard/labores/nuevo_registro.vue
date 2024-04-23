<template>  
  <FormKit type="form">
    <FormKit type="select" name="trabajador" label="Seleccione trabajador" :options="['Diego', 'Andrés', 'Maria']" />
    <FormKit type="date" name="fecha" label="Fecha" />
    <FormKit type="text" name="labor" label="Labor" />
    <FormKit type="number" name="lote" label="Lote" />
  </FormKit>
</template>