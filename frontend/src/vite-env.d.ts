/// <reference types="vite/client" />

interface ImportMetaEnv {
    readonly VITE_BACK_PORT: string
  }
  
  interface ImportMeta {
    readonly env: ImportMetaEnv
  }