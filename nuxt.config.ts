// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  srcDir: 'src/',
  components: [
    {
      path: '~/components',
      pathPrefix: false

    }
  ],
  devtools: { enabled: true },
  typescript: {
    typeCheck: true
  },
  css: ['~/assets/css/main.css'],
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
  modules: ['@formkit/nuxt','@nuxtjs/supabase', '@nuxtjs/tailwindcss', 'nuxt-lucide-icons'],
  formkit: {
    // Experimental support for auto loading (see note):
    autoImport: true
  },
  supabase: {
    redirect: false,
    redirectOptions: {
      login: '/login',
      callback: '/confirm',
      include: undefined,
      exclude: [],
      cookieRedirect: false,
    }
  }
})
