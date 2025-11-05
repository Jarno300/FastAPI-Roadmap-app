// https://nuxt.com/docs/api/configuration/nuxt-config
import { defineNuxtConfig } from "nuxt/config";

export default defineNuxtConfig({
  compatibilityDate: "2025-07-15",
  devtools: { enabled: true },
  pages: true,
  // Ensure Nuxt resolves routes from the default pages directory and uses root base URL
  srcDir: ".",
  dir: {
    pages: "pages",
  },
  app: {
    baseURL: "/",
  },
  runtimeConfig: {
    public: {
      // This will be populated from NUXT_PUBLIC_API_BASE at runtime
      apiBase: "http://localhost:8000",
    },
  },
  vite: {
    server: {
      fs: {
        allow: ["."],
      },
    },
  },
});
