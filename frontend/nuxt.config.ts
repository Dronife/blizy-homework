// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-05-15',
  devtools: { enabled: true },
  modules: ['@nuxt/eslint'],
  server: {
    host: process.env.NUXT_HOST,
    port: parseInt(process.env.NUXT_PORT)
  }
})