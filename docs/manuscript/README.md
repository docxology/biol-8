# Reproduce the BIOL-8 resource manuscript

The manuscript documents the resource types, the module coverage, and the
integrity of the flat distribution. Its evidence comes from Git paths and
object IDs in the exact course checkout.

Use Git, uv, Pandoc with matching pandoc-crossref, and XeLaTeX. From the
course checkout, register a detached worktree in a separate pinned Template
checkout.

```sh
template_dir=/absolute/path/to/template
project_dir="$template_dir/projects/working/biol-8"
git -C "$template_dir" switch --detach 87704feae0a4490ef7dad9c931d268e8c30273c2
mkdir -p "$template_dir/projects/working"
git worktree add --detach "$project_dir" HEAD
cd "$template_dir"
uv sync --locked --python 3.14 --no-dev
(cd "$project_dir" && MPLBACKEND=Agg "$template_dir/.venv/bin/python" -m docs.reproduce_inventory)
uv run --no-sync python scripts/pipeline/stage_03_render.py --project working/biol-8
uv run --no-sync python scripts/pipeline/stage_04_validate.py --project working/biol-8
```

Find the PDF, HTML, plot, and inventory receipt under
`projects/working/biol-8/output/`. [Template prerequisites](https://github.com/docxology/template/blob/87704feae0a4490ef7dad9c931d268e8c30273c2/docs/RUN_GUIDE.md)
