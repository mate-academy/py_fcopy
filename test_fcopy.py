import os
import pytest
import fcopy


@pytest.fixture
def files():
    old_file = "test1"
    new_file = "test2"
    with open(old_file, "wt") as f:
        f.write("Hello\n")
    yield old_file, new_file
    os.remove(old_file)
    os.remove(new_file)


def test_fcopy(files):
    fcopy.fcopy(*files)
    with open(files[1], 'rt') as f:
        assert f.read() == "Hello\n"