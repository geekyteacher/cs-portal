# Geeky Teacher

The Computing Portal is a static site built with [Astro](https://astro.build/).

## Requirements

- Node.js 20.19 or newer, or 22.19 or newer (Node.js 22 LTS is recommended)
- npm 9.6.5 or newer

## Getting started

If you use [nvm](https://github.com/nvm-sh/nvm), run `nvm use` to select the
version in `.nvmrc`.

Install the locked dependencies and start the local development server:

```sh
npm ci
npm run dev
```

Astro prints the local URL when the server starts. Edit pages in `src/pages/`;
each `.astro` file becomes a route.

## Commands

| Command | Description |
| --- | --- |
| `npm run dev` | Start the development server |
| `npm run build` | Build the static site into `dist/` |
| `npm run preview` | Preview the production build locally |

The site uses Astro's static output. Deploy the contents of `dist/` to your
static hosting provider.

For step-by-step guidance on writing lessons, managing shared links, adding
media, and changing styles, see the [teacher maintenance guide](docs/teacher-maintenance.md).

## Cloudflare

This project deploys as a static-assets Worker. In Cloudflare Workers Builds,
set the build command to `npm run build` and leave the deploy command as
`npx wrangler deploy`. The `wrangler.jsonc` configuration points Wrangler at
Astro's `dist/` output directory.

## Adding course content

Markdown lessons live in `content/`, grouped by course and curriculum section.
Open the repository (or `content/`) as an Obsidian vault, edit the Markdown,
and commit the changes with Git. Use standard Markdown links and image syntax;
Astro does not render Obsidian wikilinks by default.

Each lesson needs `title` and `description` frontmatter. Set `draft: true` while
writing; draft lessons are omitted from the published site. Set it to `false`
when the lesson is ready. The `order` field controls its position within a
section.

Top-level courses are listed in `src/data/courses.ts`. Lesson pages and course
navigation are generated from the collection configured in
`src/content.config.ts`. Optional school-specific links are kept separately in
`src/data/school-links.ts` and are not part of lesson Markdown.

Use GitHub-style alerts for lesson callouts:

```md
> [!NOTE]
>
> Extra information for the student.
```

Supported types are `NOTE`, `TIP`, `WARNING`, and `CHALLENGE`. Use a
`pseudocode` code fence for CAIE pseudocode examples and a `python` code fence
for Python so the site can style and highlight each language appropriately.
An H2 heading named `Answers` is rendered as a collapsed disclosure section.
