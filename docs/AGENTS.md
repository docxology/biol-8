# Agent guide — biol-8

## Layout

Content source lives alongside each rendered artifact: `course/` (syllabus,
schedule), `labs/`, `homework/`, `practice_tests/`, and `module_keys/` hold the
Markdown; `slides/`, `dashboards/`, and `ALL_FILES/` are rendered or mirrored
copies. No build config, package manifest, or test suite exists in the repo —
this is a content tree.

## Conventions observed

- The root `README.md` carries the authoritative module table (17 modules).
- Files are keyed by module number (01–17).

## Docs maintenance

- Keep `docs/` minimal: this guide, `README.md`, and
  `docs/manuscript/MANUSCRIPT_STATUS.md`. Do not duplicate the module table;
  link to the root `README.md` instead.
