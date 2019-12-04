"""Module for copying data from one file to another"""


def fcopy(filename1: str, filename2: str) -> None:
    """
    The func open one file for reading and another for writing
    :param filename1: name of text-file with data
    :param filename2: name of text-file to write
    :return: None
    """
    with open(filename1, 'r') as reader, open(filename2, 'w') as writer:
        content = reader.read()
        writer.write(content)
