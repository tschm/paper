from copier import run_copy

def test_repo(tmp_path):
    run_copy(".", tmp_path)
    for file in tmp_path.iterdir():
        for file in file.iterdir():
            #if file.is_dir():
            if file.is_file():
                print(file)
