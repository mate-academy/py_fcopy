"""
module file copy
"""


def fcopy(filename1: str, filename2: str) -> None:
    """
    Copy the contents of the file to a new file.
    :param filename1: str
    :param filename2: str
    :return: None
    """
    with open(filename1, "rt") as file_1:
        with open(filename2, "wt") as file_2:
            file_2.write(file_1.read())


def file_copy(filename1: str, filename2: str) -> None:
    """
    Copy the contents of the file to a new file.
    :param filename1: str
    :param filename2: str
    :return: None
    """
    with open(filename1, "rt") as f1, open(filename2, "wt") as f2:
        f2.write(f1.read())
