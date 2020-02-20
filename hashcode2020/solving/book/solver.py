from __future__ import annotations

from typing import List, Set

from ..abc import (
    Solver,
)
from .solution import (
    BookSolution,
)
from .models import (
    Book,
    Library,
    LibraryPlanning,
)


class BookSolver(Solver):

    @classmethod
    def from_lines(cls, raw: List[str]) -> BookSolver:
        metadata = tuple(map(int, raw[0].split()))
        days = metadata[2]
        book_scores = tuple(map(int, raw[0].split()))

        books = [Book(identifier, score) for identifier, score in enumerate(book_scores)]

        libraries = list()
        for identifier, raw_library in enumerate(raw[2:]):
            raw_library = tuple(map(int, raw_library.split()))
            library_books = [books[i] for i in raw_library]
            library = Library(identifier, library_books)
            libraries.append(library)

        books = set(books)
        libraries = set(libraries)

        assert len(books) == metadata[0]
        assert len(libraries) == metadata[1]
        return BookSolver(books, libraries, days)

    def __init__(self, books: Set[Book], libraries: Set[Library], days: int):
        self.books = books
        self.libraries = libraries
        self.days = days

    def solve(self) -> BookSolution:
        plannings = list()

        for library in self.libraries:
            planned_books = list()
            planning = LibraryPlanning(library, planned_books)
            plannings.append(planning)

        return BookSolution(plannings)
