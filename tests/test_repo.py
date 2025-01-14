import os
from pathlib import Path

import pytest
from copier import run_copy


@pytest.fixture()
def folder(tmp_path: Path) -> Path:
    return tmp_path

@pytest.fixture()
def repo(folder):
    # Assuming `run_copy` is copying a folder to `tmp_path`
    run_copy(str(Path(__file__).parent.parent), folder, data={"project_name": "maffay"}, vcs_ref="main")

    commands = [
        "git init --initial-branch=main",
        "git add --all",
        "git commit -m 'initial commit'"]

    os.chdir(folder)
    for command in commands:
        os.system(command)

    # Collect all files in the directory and return as a set of relative paths
    # Use relative_to to get the file paths relative to `tmp_path`
    return set(
        [file.relative_to(folder) for file in folder.rglob("*") if file.is_file()]
    )


def test_repo(repo):
    assert Path(".pre-commit-config.yaml") in repo
    assert Path("Makefile") in repo
    assert Path(".gitignore") in repo
    assert Path("README.md") in repo
    assert Path("paper/maffay.tex") in repo
    assert Path("paper/references.bib") in repo
    assert Path(".github/workflows/latex.yml")
    assert Path(".github/workflows/pre-commit.yml") in repo


def test_compile(folder, repo):
    assert Path(folder / "Makefile").exists()
    os.system(f"make -C {folder} install")
    os.system(f"make -C {folder} compile")

def test_help(folder, repo):
    os.system(f"make -C {folder} help")


def test_clean(folder, repo):
    os.system(f"make -C {folder} clean")


def test_fmt(folder, repo):
    os.system(f"make -C {folder} fmt")
