"""This code copies contents from one file to another"""

def fcopy(filename1: str, filename2: str) -> None:
    """
    Copy the file on line-by-line basis
    :param filename1: original file, the source for copying
    :param filename2: new file, the destination for copying
    :return: none as the result is new contents of the second file
    """
    to_be_copied = []
    with open(f"{filename1}", "rt") as func:
        for line in func:
            to_be_copied.append(line)
    with open(f"{filename2}", "wt+") as func:
        func.writelines(to_be_copied)
