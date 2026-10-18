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
