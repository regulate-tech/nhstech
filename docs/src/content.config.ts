import { defineCollection, z } from 'astro:content'
import { glob } from 'astro/loaders'

const posts = defineCollection({
  loader: glob({
    base: 'posts',
    pattern: '**/*.md',
    generateId: ({entry, data}) => {
      // Note: jekyll pulls the pubDate and the slug from filename,
      // so we recreate that here by adding the pubDate where unset
      if (!data.pubDate) {
        // first 10 chars should be a hyphenated ISO8601 date.
        data.pubDate = entry.slice(0, 10)
      }
      if (data.slug && typeof data.slug === 'string') {
        // use the `slug` prop from the frontmatter if specified.
        return data.slug
      }
      // chars after the iso date are teh slug, minus the `.md` suffix
      return entry.slice(11, -3)
    }
  }),
  schema: z.object({
    title: z.string(),
    pubDate: z.string()
  }),
})

export const collections = { posts }