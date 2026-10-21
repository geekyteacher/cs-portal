import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const lessons = defineCollection({
  loader: glob({ base: './content', pattern: '**/*.md' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    type: z.enum(['unit', 'lesson']).default('lesson'),
    order: z.number().default(0),
    draft: z.boolean().default(false),
  }),
});

export const collections = { lessons };