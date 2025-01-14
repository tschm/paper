# paper

This repository is a template for the [cradle](https://github.com/cvxgrp/cradle)
system.

The template supports the fast creation of repositories of LaTeX documents.
Out of the box you get

* curated pre-commit-hooks (e.g. for spelling)
* github ci/cd workflows
* Makefile
* Example *.tex and bib file.

```bash
    create  paper
    create  paper/references.bib
    create  paper/{{ project_name }}.tex
    create  README.md
    create  .gitignore
    create  .github
    create  .github/workflows
    create  .github/workflows/latex.yml
    create  Makefile
```

With every push into the repo the document is compiled
and published on a draft branch.

