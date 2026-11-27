"""Bind the course-resource measurements to its committed Git tree."""

from collections import Counter, defaultdict
import json
from pathlib import Path
import re
import subprocess

import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = {
    "course": "Course guides", "slides": "Lecture slides", "labs": "Lab handouts",
    "homework": "Homework", "practice_tests": "Practice exams and keys",
    "module_keys": "Module keys", "dashboards": "Review dashboards",
}


def main() -> None:
    walked = subprocess.check_output(
        ["git", "-C", str(ROOT), "ls-tree", "-r", "-z", "HEAD", "--", *CATEGORIES, "ALL_FILES"],
        text=True,
    )
    counts = Counter()
    source = defaultdict(set)
    distribution = {}
    modules = []
    for record in walked.strip("\0").split("\0"):
        entry, path = record.split("\t", 1)
        _, kind, object_id = entry.split()
        category, name = path.split("/", 1)
        if kind != "blob" or name in {"README.md", "AGENTS.md"}:
            continue
        counts[category] += 1
        if category == "ALL_FILES":
            distribution[name] = object_id
        else:
            source[name].add(object_id)
        identified = re.fullmatch(r"homework/module-(\d+)-.+-questions\.md", path)
        if identified:
            modules.append(int(identified[1]))
    flat_matches = sum(
        object_id in source.get(name, ()) for name, object_id in distribution.items()
    )
    expected = {name: next(iter(blobs)) for name, blobs in source.items() if len(blobs) == 1}
    if distribution != expected or sum(counts[name] for name in CATEGORIES) != len(distribution):
        raise ValueError("The flat teaching files differ from the source inventory.")
    if sorted(modules) != list(range(1, 18)):
        raise ValueError("Homework does not cover the recorded module identifiers.")
    lab_count = sum(name.startswith("lab-") and name.endswith(".md") for name in source)
    practice_count = sum(bool(re.fullmatch(r"practice-test-\d+\.md", name)) for name in source)
    if (lab_count, practice_count, counts["slides"], counts["dashboards"], flat_matches) != (19, 12, 15, 19, 228):
        raise ValueError("The committed teaching inventory differs from the reported counts.")

    data = ROOT / "output" / "data"
    figures = ROOT / "output" / "figures"
    data.mkdir(parents=True, exist_ok=True)
    figures.mkdir(parents=True, exist_ok=True)
    commit = subprocess.check_output(["git", "-C", str(ROOT), "rev-parse", "HEAD"], text=True).strip()
    report = {
        "source_commit": commit, "category_counts": dict(counts),
        "modules": sorted(modules), "lab_handouts": lab_count, "practice_exams": practice_count,
        "matching_distribution_files": flat_matches,
    }
    (data / "course-inventory.json").write_text(json.dumps(report, indent=2) + "\n")
    plot, axes = plt.subplots(figsize=(7.6, 4.2), layout="constrained")
    axes.barh(list(CATEGORIES.values()), [counts[name] for name in CATEGORIES], color="#315a77")
    axes.invert_yaxis()
    axes.set_xlabel("Committed files")
    plot.savefig(figures / "course-inventory.png", dpi=160)
    plt.close(plot)
    registry = {"figures": [{
        "label": "fig:course-inventory", "filename": "course-inventory.png",
        "caption": "Teaching file counts by source directory.",
        "alt_text": "Homework and module keys have the largest counts, followed by practice materials.",
        "generated_by": "python -m docs.reproduce_inventory",
    }]}
    (figures / "figure_registry.json").write_text(json.dumps(registry, indent=2) + "\n")
    print("Verified 228 distribution files and all 17 homework modules.")


if __name__ == "__main__":
    main()
