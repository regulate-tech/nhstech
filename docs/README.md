# NHS Tech Website

A static site built with [astro.build](https://astro.build)

## Project structure

- `posts` - News posts in Markdown
- `src/pages` - All other static pages. Can be .md, .html, or .astro files.
- `src/layouts` - Same as in a Jekyll, the layout templates go here as .astro files.
- `src/component` - Any other reusable templates go here as .astro files.
- `src/public` - Any other files you want to end up in the root of the site.
- `src/plugins` - Tweaks to the build process.
- `src/styles` - The global CSS, built on [tailwind](https://tailwindcss.com/)

## Commands

All commands are run from the root of the project, from a terminal:

| Command                   | Action                                           |
| :------------------------ | :----------------------------------------------- |
| `npm install`             | Installs dependencies                            |
| `npm start`               | Starts local dev server at `localhost:4321`      |
| `npm run build`           | Build your production site to `./dist/`          |
| `npm run preview`         | Preview your build locally, before deploying     |
| `npm run astro ...`       | Run CLI commands like `astro add`, `astro check` |
| `npm run astro -- --help` | Get help using the Astro CLI                     |

