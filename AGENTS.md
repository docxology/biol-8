# AGENTS.md — biol-8

Guidance for agents working in this repository.

## What this repository is

Course materials for **BIOL-8: Human Biology** at College of the Redwoods,
Spring 2026. Seventeen modules run from exploring life science through ecology
and evolution. It is taught material, not software.

Every artefact is committed in three forms — Markdown source, rendered PDF, and
DOCX — so an instructor can read the Markdown, hand out the PDF, or edit the
DOCX without a build step.

## Layout

| Path | Contents |
|---|---|
| `course/` | Syllabus and schedule (`BIOL-8_Spring-2026_Syllabus.*`, `Schedule.*`) |
| `slides/` | Lecture slides, Modules 01–15, as PDF |
| `labs/` | `lab-NN_<topic>.md` with matching `.pdf` |
| `homework/` | `module-NN-<topic>-questions` as `.md`, `.pdf`, `.docx` |
| `practice_tests/` | `practice-test-NN.md`, `_key.md`, and their PDFs |
| `module_keys/` | `module-NN-<topic>-keys-to-success` as `.md`, `.pdf`, `.docx` |
| `dashboards/` | Interactive HTML review dashboards, one per lab |
| `ALL_FILES/` | Flat duplicate of the above for single-folder distribution |
| `docs/` | Documentation hub and manuscript notes |

## Conventions

- **Triple format is the contract.** A content edit means updating the Markdown
  and regenerating the PDF and DOCX. A `.md` without its matching `.pdf`/`.docx`
  is an incomplete change.
- Numbering is the join key across folders: `lab-01` in `labs/` is the same
  session as `lab-01_...-dashboard.html` in `dashboards/`. Keep numbering
  aligned; do not renumber an existing module, because students and the syllabus
  reference the numbers.
- Practice-test answer keys live beside the test as `_key` files. Keep keys out
  of student-facing PDFs.
- `ALL_FILES/` is generated distribution material. Treat it as derived: update
  the source folder, then refresh the flat copy, rather than editing it directly.
- Content is instructional. Accuracy review matters more than style; a wrong
  physiological claim in a slide is a defect.

## Verification

There is no build, test suite, or CI. Verify by opening the regenerated PDF/DOCX
for the module you touched and confirming the Markdown, PDF, and DOCX agree.
Report which module and which formats you checked.
