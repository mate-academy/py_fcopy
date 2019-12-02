'''
Module
'''


def fcopy(read_file: str, write_file: str) -> None:
    '''
    Read text from read_file adn write this text in write_file
    :param read_file:
    :param write_file:
    :return:
    '''
    with open(read_file, "rt") as reading:
        with open(write_file, "wt") as writing:
            for line in reading:
                writing.write(line)
