"""Copy file module"""

def fcopy(filename1: str, filename2: str) -> None:
    """
    :param filename1: Open filename1 for reading
    :param filename2: Open filename2 for writing
    :return: None
    """
    with open(filename1, 'rt') as file_1:
        with open(filename2, 'wt') as file_2:
            file_2.write(file_1.read())
