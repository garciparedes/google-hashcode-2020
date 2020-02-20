from __future__ import annotations

from typing import List


class Book(object):
    def __init__(self, identifier: int, score: int):
        self.identifier = identifier
        self.score = score


class Library(object):

    def __init__(self, identifier: int, books: List[Book]):
        self.identifier = identifier
        self.books = books


class LibraryPlanning(object):

    def __init__(self, library: Library, books: List[Book]):
        self.library = library
        self.books = books

    @property
    def identifier(self) -> int:
        return self.library.identifier

    @property
    def book_identifiers(self) -> List[int]:
        return [book.identifier for book in self.books]