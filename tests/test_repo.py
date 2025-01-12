import pytest
from copier import run_copy


pytest.fixture()
def repo(tmpdir):
    run_copy(".", tmp_path, data={"project_name": "maffay"})
    return tmpdir

def test_repo(repo):
    #run_copy(".", tmp_path, data={"project_name": "maffay"})

    set([file for file in repo.rglob("*")])



    #    for file in file.iterdir():
    #        print(file)
