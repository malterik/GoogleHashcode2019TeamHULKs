
def _read_file_line_by_line(filepath: str):
    """
    Read file line by line
    :param filepath:
    :return: List of all lines
    """
    with open(filepath) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    return content


def load_data(filepath: str):
    """
    Loads data from file and return it in a structured manner
    :param filepath:
    :return:
    """
    raw = _read_file_line_by_line(filepath)
    data = {}
    data = raw
    return data


def create_solution_file(solution, solution_path: str):
    file = open(solution_path, "w")
    file.write("This is the solution:")
    file.write(solution)
    file.close()
