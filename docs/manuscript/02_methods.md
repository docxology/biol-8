# Methods

The replay reads the committed tree for the course, slides, lab handouts,
homework, module keys, practice tests, and dashboard directories. It excludes
directory guidance files. It groups teaching artifacts by path and format.
The homework filenames provide consecutive module identifiers.

For each flat distribution file, the replay compares its basename and blob
identifier with the source index. It verifies that every source artifact has a
matching distribution entry. The exact commit, category counts, and matching
totals are recorded in the generated receipt.
