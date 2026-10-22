# Teacher's guide to the Computing Portal

This guide explains how to add and update lesson content, use images and other
media, and make site-wide style changes. The portal is built with Astro; most
lesson updates only require editing Markdown files.

## Quick start

1. Open the project in your editor, or open the `content/` folder as an Obsidian
   vault.
2. Install the project dependencies once with `npm ci`.
3. Start the local preview with `npm run dev`.
4. Open the local URL printed in the terminal and keep it open while editing.
   The preview updates when files are saved.
5. When finished, check the changes and share them through the school's usual
   Git workflow.

You need Node.js 20.19 or newer (or 22.19 or newer) and npm 9.6.5 or newer.
See [README.md](./README.md) for setup and deployment details.

## Where lesson files go

Lessons are Markdown files inside `content/`, grouped first by course and then,
where useful, by topic:

```text
content/
  year5/
    start-here.md
    programming/
      scratch-game-mechanics/
        index.md
        lesson-1-loops-and-patrol-enemies.md
  igcse/
    programming/
      variables.md
```

Use an existing course folder such as `year5`, `year9`, `igcse`, or `alevel`.
The folder immediately below the course is used as the navigation section. For
example, `content/igcse/programming/variables.md` appears under GCSE Computer
Science > Programming.

The filename becomes part of the page address. For example,
`content/igcse/programming/variables.md` is shown at
`/igcse/programming/variables/`. An `index.md` inside a topic folder is the
topic's landing page; sibling Markdown files become pages within that topic.
Use lowercase names and hyphens, and avoid renaming a published file unless
you are happy for its page address to change.

## Writing or editing a lesson

Every content page starts with YAML frontmatter between `---` lines. It must
include a title and a short description:

```md
---
title: Variables
description: Store, update, and use data in a program.
order: 1
draft: true
---
```

Fields:

| Field | What it does |
| --- | --- |
| `title` | Page title shown to students and in navigation. Required. |
| `description` | Short summary shown on the page or course listing. Required. |
| `order` | Position within the section; lower numbers appear first. Defaults to `0`. |
| `draft` | Use `true` while working; draft pages do not appear on the site. Set to `false` when ready. Defaults to `false`. |
| `type` | Optional `lesson` or `unit` label. It currently does not change how a page is displayed. |

After the frontmatter, use Markdown for the lesson. The site already displays
the title from the frontmatter, so start the lesson with an H2 (`##`) rather
than another H1 (`#`).

```md
## Learning goals

- Explain the key idea.
- Apply it to an example.

## Explanation

Write short sections with clear headings. Use **bold** for important terms
and `backticks` for code, commands, or variable names.

## Practice

Add questions or an activity for students to try.
```

Markdown links and images use the standard syntax. Obsidian wikilinks such as
`[[Another page]]` are not converted into working links by the site.

### Useful Markdown features

**Lists**

```md
- First point
- Second point

1. First step
2. Second step
```

**Tables**

```md
| Term | Meaning |
| --- | --- |
| Input | Data provided to a program |
| Output | Information produced by a program |
```

**Callouts** — supported types are `NOTE`, `TIP`, `WARNING`, and `CHALLENGE`.
Keep the blank quote line after the marker:

```md
> [!TIP]
>
> Try tracing the value after each instruction.
```

**Code examples** — use a language label after the opening backticks.
`pseudocode` is specially highlighted and labelled for CAIE examples; `python`
uses the normal Python syntax highlighting.

````md
```pseudocode
OUTPUT "Hello"
```

```python
print("Hello")
```
````

**Answers** — an H2 heading written exactly as `## Answers` turns that section,
up to the next H2, into a collapsed disclosure. Put answers after the questions
and do not use that heading for anything you do not want hidden.

## Adding images and other media

Put files that belong to the site in `public/`. The existing folders are
`public/images/` for images and `public/downloads/` for documents and
worksheets. Create another folder under `public/` if needed, such as
`public/videos/`. Give files descriptive, lowercase names, for example
`binary-search-trace.png`.

In lesson Markdown, refer to public files from the site root (start the path
with `/`), not relative to the Markdown file:

```md
![A flowchart showing a decision and two possible branches](/images/decision-flowchart.png)

[Download the practice worksheet](/downloads/search-practice.pdf)
```

Write useful alt text that describes the information in an image. For a purely
decorative image, use empty alt text (`![](/images/decorative-divider.png)`).
Use common web formats such as PNG, JPEG, or WebP, and resize/compress large
images before adding them. Do not put private student information or material
you do not have permission to publish on the site.

For a video hosted in `public/videos/`, HTML5 video can be added in a Markdown
file. Keep a blank line before and after the HTML block:

```html
<video controls preload="metadata" width="720">
  <source src="/videos/demo.mp4" type="video/mp4" />
  Your browser does not support embedded video.
</video>
```

For externally hosted media, a normal Markdown link is the most dependable
option. If you use an embed, check that the provider permits it, that it works
in the local preview, and that students who cannot use the embed have an
alternative link or description. Avoid autoplay.

## Changing the site's appearance

Site-wide CSS is in `src/styles/global.css`. Most lesson styling is grouped
under `.lesson-content`; changing a broad selector such as `a`, `body`, or
`:root` may affect pages beyond lessons. Save the CSS and check the affected
pages in the local preview at both desktop and mobile widths.

The `:root` block near the top of the stylesheet contains shared colours such
as `--accent`, `--surface`, and `--muted`. Prefer changing these variables
when a whole-site colour needs to change. For a lesson-specific element, add a
rule under `.lesson-content` so it does not unintentionally alter navigation
or other site components.

For example, this rule keeps lesson images and videos within the content
column:

```css
.lesson-content img,
.lesson-content video {
  max-width: 100%;
  height: auto;
}
```

The page layout and shared site shell live in `src/layouts/` and reusable
components live in `src/components/`. Changes there affect how pages are
structured, so ask the person maintaining the site before changing them if you
only need to update lesson material.

## Checking and publishing changes

Before marking a page ready:

- Set `draft: false`.
- Check spelling, links, image descriptions, and code examples.
- Open the page in the local preview and follow its links.
- Check that images and downloads load, including on a narrow/mobile screen.
- Run `npm run build` to check that the site can be generated.

The build output is written to `dist/`; do not edit files in that generated
folder. Changes are published through the project's normal Git and deployment
workflow.

## Common problems

- **A page is missing:** Check that its `draft` value is `false`, its file is
  under an existing course folder, and its frontmatter is valid.
- **A page appears in the wrong order:** Adjust its numeric `order`. Pages with
  the same order are sorted by title.
- **An image or download is broken:** Confirm the file is under `public/` and
  the Markdown path starts with `/` and matches the filename's spelling and
  capitalization exactly.
- **A link does not work:** Use a regular Markdown link, and check that the
  destination page or file exists. Obsidian wikilinks are not supported.
- **A style change affects too much:** Narrow the CSS selector, for example by
  prefixing it with `.lesson-content`, and check other pages before publishing.
