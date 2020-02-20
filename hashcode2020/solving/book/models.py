from __future__ import annotations

from typing import List, Iterable, Set
import operator as op

from cached_property import cached_property


class Book(object):
    def __init__(self, identifier: int, score: int):
        self.identifier = identifier
        self.score = score


class Library(object):

    def __init__(self, identifier: int, signup_days: int, books_per_days: int, books: Set[Book]):
        self.identifier = identifier
        self.signup_days = signup_days
        self.books_per_days = books_per_days
        self.books = books

    @cached_property
    def available_score(self) -> int:
        return sum((book.score for book in self.books), 0)

    @cached_property
    def sorted_books(self) -> List[Book]:
        return sorted(self.books, key=op.attrgetter('score'))


class LibraryPlanning(object):

    def __init__(self, library: Library, books: Set[Book] = None):
        if books is None:
            books = set()
        self.library = library
        self.books = books

    @property
    def identifier(self) -> int:
        return self.library.identifier

    @property
    def score(self) -> int:
        return sum((book.score for book in self.books), 0)

    @property
    def book_identifiers(self) -> List[int]:
        return [book.identifier for book in self.books]

    def insert_possible_books(self, available_books: Set[Book], available_days: int):
        available_days -= self.library.signup_days
        available_books = available_books & self.library.books

        available_books = sorted(available_books, key=op.attrgetter('score'), reverse=True)
        available_books_iter = iter(available_books)
        while available_days > 0:
            for _ in range(self.library.books_per_days):
                book = next(available_books_iter, None)
                if book is None:
                    return
                self.books.add(book)
            available_days -= 1
