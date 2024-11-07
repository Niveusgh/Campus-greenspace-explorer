// vite.config.js
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  build: {
    outDir: 'static/js/react/dist',
    rollupOptions: {
      input: 'static/js/react/mapApp.jsx',
      output: {
        entryFileNames: 'mapApp.js',
      }
    }
  },
  server: {
    proxy: {
      '/api': 'http://localhost:5000'
    }
  }
});