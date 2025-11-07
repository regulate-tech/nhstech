export function defaultMarkdownLayout () {
  return function (_, file) {
    const layout = file.data.astro.frontmatter.layout
    if (!layout || layout === 'default') {
      file.data.astro.frontmatter.layout = "../layouts/default.astro";
    }
  }
}
