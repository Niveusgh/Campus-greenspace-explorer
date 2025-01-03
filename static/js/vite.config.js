import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

export default defineConfig({
  plugins: [react()],
  root: './static/js/react',
  base: './',
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './components')
    }
  }
})