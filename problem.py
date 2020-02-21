import typing as ty

class Library:
    books = []
    days_to_sign_up = 0
    books_per_day = 0
    id = 0

    def __init__(self, id: int, books, days_to_sign_up, books_per_day):
        self.books = books
        self.days_to_sign_up = days_to_sign_up
        self.books_per_day = books_per_day
        self.id = id

    def __repr__(self):
        return "books: {}\n days_to_sign_up: {}\n books_per_day: {}".format(self.books, self.days_to_sign_up, self.books_per_day)


class Problem:
    number_of_days = 0
    libraries: ty.List[Library] = []
    book_scores: ty.List[int] = []

    def __init__(self, number_of_days: int, book_scores: ty.List[int], libraries: ty.List[Library]):
        self.number_of_days = number_of_days
        self.book_scores = book_scores
        self.libraries = libraries

    def __repr__(self):
        return "number_of_days: {}\n libraries: \n{}\n book_scores: {}".format(self.number_of_days, self.libraries, self.book_scores)
