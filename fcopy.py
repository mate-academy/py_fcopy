"""docstring"""


def fcopy(filename1: str, filename2: str) -> None:
    """read information from file1 and write to file2"""
    file_read = open(filename1)
    file_write = open(filename2, 'w')
    for i in file_read:
        file_write.write(i)
