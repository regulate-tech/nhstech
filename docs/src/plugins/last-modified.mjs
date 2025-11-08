// see: https://docs.astro.build/en/recipes/modified-time/
import { execSync } from "node:child_process";

export function gitLastModified () {
  return function (tree, file) {
    const filepath = file.history[0];
    const result = execSync(`git log -1 --pretty="format:%cI" "${filepath}"`);
    file.data.astro.frontmatter.lastModified = result.toString();
  };
}
