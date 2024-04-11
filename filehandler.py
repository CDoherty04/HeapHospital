def file_handler(filename):
    """Takes a file and generates instructions from it"""

    with open(filename, "r") as file:
        lines = file.readlines()

    # Removes newlines
    lines = [line.strip() for line in lines]
    return lines
