"""docstring"""


def fcopy(filename1: str, filename2: str) -> None:
    """read information from file1 and write to file2"""
    with open(filename1, 'rt') as file_read:
        with open(filename2, 'wt') as file_write:
            for i in file_read:
                file_write.write(i)
