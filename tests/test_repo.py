import pytest
from copier import run_copy


@pytest.fixture()
def repo(tmp_path):
    run_copy(".", tmp_path, data={"project_name": "maffay"})
    return set([file for file in tmp_path.rglob("*")])

def test_repo(repo):
    #run_copy(".", tmp_path, data={"project_name": "maffay"})

	print(repo)
	assert False



    #    for file in file.iterdir():
    #        print(file)
