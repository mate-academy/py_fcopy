"""module docstring"""


def fcopy(filename1: str, filename2: str) -> None:
    """read line by line from file1 and write line by line to file2"""
    with open(filename1, "rt") as old_file:
        with open(filename2, "wt") as new_file:
            for line in old_file:
                new_file.write(line)
