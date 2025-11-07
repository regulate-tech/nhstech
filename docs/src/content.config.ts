import { defineCollection, z } from 'astro:content'
import { glob } from 'astro/loaders'

const posts = defineCollection({
  loader: glob({
    base: 'posts',
    pattern: '**/*.md',
    generateId: ({entry, data}) => {
      const id = entry.slice(11, -3)
      const pubDate = data.pubDate ?? entry.slice(0, 10)
      // Note: mutating the data obj. serves them right for passing it in unfrozen.
      data.pubDate = pubDate
      return id
    }
  }),
  schema: z.object({
    title: z.string(),
    pubDate: z.string().optional()
  }),
})

export const collections = { posts }