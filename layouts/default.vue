<template>
  <div class="flex flex-col bg-slate-500 h-[100vh] ">

    <header class="flex justify-between">
      <NuxtLink to="/dashboard">
        Dashboard
      </NuxtLink>

      <div>

      </div>
      Nombre del usuario
    </header>

    <div class="flex-grow bg-gray-300 flex">
      <aside class="w-[300px] flex flex-col">
          <NuxtLink to="/dashboard">Dashboard</NuxtLink>
          <NuxtLink to="/dashboard/labores">Labores</NuxtLink>
      </aside>
      <main class="w-[100%] bg-red-50">
        <slot />
      </main>
    </div>

    <footer>
      footer
    </footer>
  </div>
</template>