from problem import *
from solution import *

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
    first_line = raw[0].split(" ")
    number_of_books = int(first_line[0])
    number_of_libraries = int(first_line[1])
    number_of_days = int(first_line[2])

    book_scores = [0] * number_of_books
    for i, book_score in enumerate(raw[1].split(" ")):
        book_scores[i] = int(book_score)

    libraries = []

    i = 2
    while (i < len(raw)):
        row = raw[i].split(" ")
        books_in_library = int(row[0])
        days_to_sign_up = int(row[1])
        books_per_day = int(row[2])
        i += 1
        row = raw[i].split(" ")
        books_in_library = [int(book) for book in row]
        i += 1
        libraries.append(Library(books_in_library, days_to_sign_up, books_per_day))

    problem = Problem(number_of_days, book_scores, libraries)
    return problem


def create_solution_file(solution: Solution, solution_path: str):
    file = open(solution_path, "w")
    file.write(str(solution.number_of_libraries) + "\n")
    for entry in solution.libraries:
        file.write(str(entry.id) + " " + str(entry.number_of_books) + "\n")
        for book in entry.books_to_scan:
            file.write(str(book) + " ")
        file.write("\n")
    file.close()
