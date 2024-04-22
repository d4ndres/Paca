<template>
  <div>
    <header>
      <NuxtLink to="/dashboard">
        Dashboard
      </NuxtLink>

      <div>

      </div>
      Nombre del usuario
    </header>
    <div>
      <aside>
          <NuxtLink to="/dashboard">Dashboard</NuxtLink>
          <NuxtLink to="/dashboard/labores">Labores</NuxtLink>
      </aside>
      <main>
        <slot />
      </main>
    </div>
    <footer>
      footer
    </footer>
  </div>
</template>