# Teacher's guide to maintaining the Computing Portal

This guide explains how to update course pages, lessons, links, styles, and media in this repository. The portal is a static website: its pages are generated from the files here and published as a build. Editing a file does not publish it by itself.

Use VS Code or another text editor to edit files in your local copy of this repository. If you use Obsidian, open the repository (or its `content/` folder) as a vault. Save new lessons in `content/` and media in `public/media/`, not in a separate notes folder or the generated `dist/` folder.

## 1. Where things live

| What you want to change | Where to work |
| --- | --- |
| Course and lesson text | `content/` |
| Courses shown on the home page | `src/data/courses.ts` |
| Student-facing school or shared-folder links | `src/data/school-links.ts` |
| Site colours, layout, and responsive styles | `src/styles/global.css` |
| Header, footer, navigation, and page layout | `src/components/`, `src/layouts/`, and `src/pages/` |
| Images, PDFs, and other files served unchanged | `public/media/` (create the folders if needed) |

The `assets/css/styles.css` file is not the active site stylesheet. The site imports `src/styles/global.css` from `src/layouts/BaseLayout.astro`.

## 2. Create or edit a lesson

### Choose the file location

Put Markdown files under `content/`, inside a folder named for the course slug. Use lowercase names and hyphens rather than spaces. The folder structure determines the page URL and the section in course navigation.

```text
content/
  year5/
    programming/
      scratch-game-mechanics/
        index.md
        lesson-1-loops-and-patrol-enemies.md
  igcse/
    programming/
      variables.md
```

For example:

- `content/igcse/programming/variables.md` becomes `/igcse/programming/variables`.
- `content/year5/programming/scratch-game-mechanics/index.md` becomes `/year5/programming/scratch-game-mechanics`.
- A lesson next to that `index.md` becomes `/year5/programming/scratch-game-mechanics/lesson-1-loops-and-patrol-enemies`.
- A file directly under a course folder, such as `content/year8/intro.md`, is grouped under the `Lessons` section.

An `index.md` inside a unit folder is useful as a unit introduction. Use `type: unit` for it. The site displays units on the course landing page when a course has units; individual published lesson pages are also listed in the course navigation.

### Add the required frontmatter

Every content file needs a title and a short description between the opening and closing `---` lines:

```md
---
title: Variables
description: Store, update, and use data in a program.
type: lesson
order: 1
draft: true
---

Introduce the topic here.
```

Fields:

- `title` and `description` are required.
- `type` is `lesson` by default. Use `type: unit` for a unit overview.
- `order` is a number used to order pages within a section (lower numbers appear first). Pages with the same order are sorted by title.
- `draft` defaults to `false`, so explicitly set `draft: true` while preparing new material. Draft pages are not published or listed. Change it to `false` only when the lesson is ready.

The page template already displays the frontmatter title as the page heading. Start the body with an introduction or an `##` heading rather than repeating the title as another `#` heading.

### Write the lesson body

Use standard Markdown. A short example:

````md
## Learning goals

- Explain what a variable stores.
- Trace how a variable's value changes.

## Worked example

```python
score = 0
score = score + 1
```

> [!TIP]
>
> Ask students to predict the value before running the code.

## Answers

The answer to the practice question goes here.
````

Formatting supported by the site:

- Headings: `##` and `###` are useful for lesson sections.
- Lists: use `-` for bullets and `1.` for numbered steps.
- Links: `[description](https://example.com)` or `[another lesson](./another-lesson)`.
- Tables: use standard Markdown pipe tables for short comparisons.
- Callouts: use `> [!NOTE]`, `> [!TIP]`, `> [!WARNING]`, or `> [!CHALLENGE]` on the first line of a blockquote.
- Code: use fenced code blocks and label them with the language, for example `python` or `pseudocode`.
- Answers: an H2 heading whose text is exactly `Answers` is converted into a collapsed disclosure. Content under it remains collapsed until a student opens it.

Obsidian wikilinks such as `[[Variables]]` are not converted into links. Use normal Markdown links instead.

### Ordering and course sections

The folder immediately below the course folder determines the section. For example, `content/igcse/algorithms/binary-search.md` is in the Algorithms section. Section names are made readable from their folder names and are normally sorted alphabetically. IGCSE sections have a fixed order in `src/data/curriculum.ts`. Within a section, `order` is used first and title second.

## 3. Add images, documents, and other media

Place files that should be served as-is in `public/media/`. Astro copies files in `public/` into the published site without processing them. Keep media names short, lowercase, and hyphenated, for example `binary-search-example.png`.

Create a folder as needed:

```text
public/
  media/
    binary-search-example.png
    worksheet.pdf
```

Reference a file from Markdown using a site-root URL:

```md
![A worked binary search example](/media/binary-search-example.png)

[Download the worksheet](/media/worksheet.pdf)
```

Write useful alternative text between the image brackets so students using assistive technology understand the image. Keep image sizes reasonable for students' devices and check that the image and page are appropriate to publish. URL paths, including filename capitalization, must match the actual files.

For videos, prefer a link to the approved video or learning resource rather than adding a raw iframe. Check that the resource opens for students and does not require teacher-only permissions. Do not add private student work or personal information to the public media folder.

## 4. Change colours and styles

The active stylesheet is `src/styles/global.css`. It contains site-wide rules, lesson content rules, responsive layout rules, and CSS variables near the top of the file. For a site-wide colour adjustment, update the existing variables (such as `--surface`, `--muted`, `--accent`, and the callout colours) rather than replacing individual colour values throughout the file.

For a component-specific change, find its class in the relevant component or layout and edit the corresponding selector in `global.css`. Lesson body styles are scoped under `.lesson-content`; for example, `.lesson-content h2` changes lesson section headings. The `@media (max-width: 720px)` block controls small-screen layout, so check that changes work on both desktop and mobile widths.

Avoid broad selectors that could unintentionally change unrelated pages. Keep text readable against the background, retain visible link and focus states, and preview any changes before publishing. If a style cannot be expressed by editing an existing rule, a small class/style change may also be needed in the matching Astro component.

## 5. Add a course

Adding a content folder alone does not add a course to the home page. To create a new course:

1. Add an entry to the `courses` array in `src/data/courses.ts`. Use a lowercase URL slug such as `year10`, a display title, and a short description.
2. Create `content/<slug>/` and add the course's Markdown files there.
3. Give each page the required frontmatter, and set `draft: false` only for pages ready to publish.
4. Add course-specific student links to `src/data/school-links.ts` if needed; the object key must exactly match the course slug.
5. Run the local preview and build checks described below.

The existing course list and URLs are generated from `src/data/courses.ts`. Changing a course slug changes its URLs, so update any links to that course as well.

## 6. Add or change student shared-folder links

Edit `src/data/school-links.ts`. Links are grouped by course slug, and each course can have any number of links. For example:

```ts
export const schoolLinks: Partial<Record<string, SchoolLink[]>> = {
  year8: [
    {
      label: 'Year 8 shared resources',
      href: 'https://example.com/shared-folder',
    },
    {
      label: 'Submit Year 8 work',
      href: 'https://example.com/submit-work',
    },
  ],
  igcse: [
    {
      label: 'IGCSE revision folder',
      href: 'https://example.com/igcse-revision',
    },
  ],
};
```

Use the real course slug (for example `year8` or `igcse`) as the key. Each entry needs a student-friendly `label` and an `href`; use the complete shared URL supplied by the service. The links appear in the sidebar on pages for that course. An empty list or a course with no entry has no school-links section.

Before publishing a shared link, test it as a student would: confirm it opens the intended folder and that its sharing permissions are correct. Grant only the access students need, avoid putting passwords or access tokens into this repository, and remove or replace old links when they are no longer valid.

## 7. Preview, check, and publish

You need Node.js 20.19 or newer (or 22.19 or newer) and npm. From a terminal in the repository:

```sh
npm ci
npm run dev
```

Open the local URL printed by Astro. Check the home page, the course landing page, the new content, links, images, and a narrow/mobile-width view. Stop the development server with Ctrl+C when finished.

Before publishing, run:

```sh
npm run build
```

The generated static site is written to `dist/`. The Cloudflare deployment configuration serves that output; follow the site's normal publishing workflow to deploy it. A successful local build checks that the content can be processed, but it does not verify external link permissions, so test shared links separately.

The `npm run preview` command serves the built site locally, which is useful for checking the production output after a successful build.

Save your edits in the repository and use the school's normal Git/GitHub review and publishing process to send them live. The local development server and a successful build do not deploy the site.

## 8. Files to treat carefully

- `src/content.config.ts` defines the allowed content fields and validates every Markdown file. If you add frontmatter fields, they must also be added to its schema.
- `src/data/curriculum.ts` controls how course sections and lesson ordering are built.
- `src/pages/` and `src/layouts/` define routes and page templates. Editing these is site development, not ordinary lesson editing.
- `dist/`, `.astro/`, and `node_modules/` are generated or installed files; do not edit them by hand.
- Never put secrets, student personal data, or private resources in public content or media.
