"""Copy the contents of the file to a new file."""


def fcopy(first_file_name: str, second_file_name: str) -> str:
    """Function to copy the content of one file to another """
    with open(first_file_name, 'r') as file1:
        content_to_copy = file1.read()
    with open(second_file_name, 'w') as file2:
        file2.write(content_to_copy)
    return content_to_copy
