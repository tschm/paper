import pytest
from copier import run_copy


@pytest.fixture()
def repo(tmp_path):
    run_copy(".", tmp_path, data={"project_name": "maffay"})
    return tmp_path

def test_repo(repo):
    #run_copy(".", tmp_path, data={"project_name": "maffay"})

    s = set([file for file in repo.rglob("*")])
	print(s)
	assert False



    #    for file in file.iterdir():
    #        print(file)
