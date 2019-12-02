"""
fcopy module
Functions:
    fcopy(filename1, filename2) -- copy content
of filename1 file to filename2.
"""


def fcopy(filename1: str, filename2: str) -> None:
    """
    Copy content of the file filename1 to
    file filename2
    :param filename1: str
    :param filename2: str
    :return: None
    """
    with open(filename1, 'r') as file:
        context = file.read()

    with open(filename2, 'w') as file:
        file.write(context)
