"""
fcopy
"""


def fcopy(filename1: str, filename2: str) -> None:
    """
    fcopy
    """
    with open(filename1, 'r') as file1, open(filename2, 'w') as file2:
        file2.write(file1.read())
