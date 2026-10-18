export const courses = [
  {
    slug: 'year5',
    title: 'Year 5',
    description: 'Computing resources and activities for Year 5.',
  },
  {
    slug: 'year6',
    title: 'Year 6',
    description: 'Computing resources and activities for Year 6.',
  },
  {
    slug: 'year7',
    title: 'Year 7',
    description: 'Computing resources and activities for Year 7.',
  },
  {
    slug: 'year8',
    title: 'Year 8',
    description: 'Computing resources and activities for Year 8.',
  },
  {
    slug: 'year9',
    title: 'Year 9',
    description: 'Computing resources and activities for Year 9.',
  },
  {
    slug: 'igcse',
    title: 'GCSE Computer Science',
    description: 'Programming, algorithms, data representation, and networks.',
  },
  {
    slug: 'alevel',
    title: 'A Level Computer Science',
    description: 'Course materials and learning resources for A Level Computer Science.',
  },
] as const;

export type Course = (typeof courses)[number];