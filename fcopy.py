"""
docstring
"""


def fcopy(filename1: str, filename2: str) -> None:
    """

    :param filename1:
    :param filename2:
    :return:
    """
    with open(filename1) as file1:
        lines = file1.readlines()
        with open(filename2, "w") as file2:
            file2.writelines(lines)
