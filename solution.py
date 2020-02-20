import typing as ty

class SolutionEntry:
    id: int = 0
    number_of_books: int = 0
    books_to_scan: ty.List[int] = []

    def __init__(self, id: int, number_of_books: int, books_to_scan: ty.List[int]):
        self.id = id
        self.number_of_books = number_of_books
        self.books_to_scan = books_to_scan

    def __repr__(self):
        return "id: {}".format(self.id)

class Solution:
    number_of_libraries: int = 0
    libraries: ty.List[SolutionEntry] = []

    def __init__(self, number_of_libraries, libraries: ty.List[SolutionEntry]):
        self.number_of_libraries = number_of_libraries
        self.libraries = libraries
