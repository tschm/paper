import pytest
from copier import run_copy


@pytest.fixture()
def repo(tmp_path):
    # Assuming `run_copy` is copying a folder to `tmp_path`
    run_copy(".", tmp_path, data={"project_name": "maffay"})

    # Collect all files in the directory and return as a set of relative paths
    # Use relative_to to get the file paths relative to `tmp_path`
    return set(
        [file.relative_to(tmp_path) for file in tmp_path.rglob("*") if file.is_file()]
    )


def test_repo(repo):
    #run_copy(".", tmp_path, data={"project_name": "maffay"})

	print(repo)
	assert False



    #    for file in file.iterdir():
    #        print(file)
