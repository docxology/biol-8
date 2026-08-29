# Agent guide — biol-8

## Layout

Content source lives in `course/` (Markdown, one module per unit); everything
else (`slides/`, `labs/`, `homework/`, `practice_tests/`, `module_keys/`,
`dashboards/`) is teaching artifacts organized by type. No build config,
package manifest, or test suite exists in the repo — this is a content tree.

## Conventions observed

- The root `README.md` carries the authoritative module table (15 modules).
- Files are keyed by module number (01–15).

## Docs maintenance

- Keep `docs/` minimal: this guide, `README.md`, and
  `docs/manuscript/MANUSCRIPT_STATUS.md`. Do not duplicate the module table;
  link to the root `README.md` instead.
