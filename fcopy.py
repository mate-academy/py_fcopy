"""
Copy the contents of the file to a new file
"""


def fcopy(filename1: str, filename2: str) -> None:
    """Copy the contents in a new file"""
    with open(filename1, 'rt') as rfile:
        strg = rfile.read()

    with open(filename2, 'wt') as wfile:
        wfile.write(strg)
