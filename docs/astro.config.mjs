// @ts-check
import { defineConfig, fontProviders } from 'astro/config';
import { gitLastModified } from './src/plugins/last-modified.mjs'
import { defaultMarkdownLayout } from './src/plugins/layout.mjs'
import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  site: 'https://nhstech.uk',
  vite: {
    plugins: [tailwindcss()]
  },
  markdown: {
    remarkPlugins: [defaultMarkdownLayout, gitLastModified]
  },
  experimental: {
    fonts: [{
      provider: fontProviders.google(),
      name: 'Courier Prime',
      cssVariable: "--font-courier-prime",
      fallbacks: ["ui-monospace", "SFMono-Regular", "Menlo", "Monaco", "Consolas", "Liberation Mono", "Courier New", "monospace"],
      styles: ["normal"],
      subsets: ["latin"]
    }, {
      provider: fontProviders.google(),
      name: 'Inter',
      cssVariable: "--font-inter",
      fallbacks: ["ui-sans-serif", "system-ui", "sans-serif", "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"],
      weights: ["400 800"],
      subsets: ["latin"]
    }]
  }
})
