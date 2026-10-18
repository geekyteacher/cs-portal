import type { CollectionEntry } from 'astro:content';

type Lesson = CollectionEntry<'lessons'>;

export interface CurriculumSection {
  slug: string;
  title: string;
  lessons: Lesson[];
}

const igcseSectionOrder = [
  'programming',
  'algorithms',
  'data-representation',
  'networks',
];

function formatSectionTitle(slug: string) {
  return slug
    .split('-')
    .map((word) => word[0].toUpperCase() + word.slice(1))
    .join(' ');
}

export function groupLessons(courseSlug: string, lessons: Lesson[]) {
  const groups = new Map<string, Lesson[]>();

  for (const lesson of lessons) {
    const parts = lesson.id.split('/');
    const sectionSlug = parts.length > 2 ? parts[1] : 'lessons';
    const sectionLessons = groups.get(sectionSlug) ?? [];
    sectionLessons.push(lesson);
    groups.set(sectionSlug, sectionLessons);
  }

  return [...groups.entries()]
    .sort(([first], [second]) => {
      if (courseSlug === 'igcse') {
        return igcseSectionOrder.indexOf(first) - igcseSectionOrder.indexOf(second);
      }

      return first.localeCompare(second);
    })
    .map(([slug, sectionLessons]): CurriculumSection => ({
      slug,
      title: slug === 'lessons' ? 'Lessons' : formatSectionTitle(slug),
      lessons: sectionLessons.sort(
        (first, second) =>
          first.data.order - second.data.order || first.data.title.localeCompare(second.data.title),
      ),
    }));
}