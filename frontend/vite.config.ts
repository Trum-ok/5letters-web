import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [react()],
    build: {
      rollupOptions: {
        input: {
          main: "./index.html",
          env: "./src/public/env.js"
        },
        output: {
          entryFileNames: "assets/[name]-[hash].js",
          assetFileNames: "assets/[name]-[hash][extname]"
        }
      }
    },
    preview: {
        host: true,
        port: 3001,
    }
})
