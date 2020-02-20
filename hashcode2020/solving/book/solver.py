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
        book_scores = tuple(map(int, raw[1].split()))

        books = [Book(identifier, score) for identifier, score in enumerate(book_scores)]

        libraries = list()

        raw_libraries = list()
        rows = list(raw[2:])
        while any(rows):
            raw_library = [tuple(map(int, rows.pop(0).split())), tuple(map(int, rows.pop(0).split()))]
            raw_libraries.append(raw_library)

        for identifier, raw_library in enumerate(raw_libraries):
            # book_count = raw_library[0][0]
            signup_days = raw_library[0][1]
            books_per_days = raw_library[0][2]

            library_books = set(books[i] for i in raw_library[1])
            library = Library(identifier, signup_days, books_per_days, library_books)
            libraries.append(library)

        books = set(books)
        libraries = set(libraries)

        assert len(books) == metadata[0]
        assert len(libraries) == metadata[1]
        return BookSolver(books, libraries, days)

    def __init__(self, books: Set[Book], libraries: Set[Library], available_days: int):
        self.books = books
        self.libraries = libraries
        self.available_days = available_days

    def solve(self) -> BookSolution:
        k_library = list()

        for library in self.libraries:
            k = library.available_score
            k_library.append((k, library))

        sorted_libraries = [x[1] for x in sorted(k_library, key= lambda x: x[0])]

        available_books = self.books
        plannings = list()

        for library in sorted_libraries:
            planning = LibraryPlanning(library)
            planning.insert_possible_books(available_books, self.available_days)
            if not any(planning.books):
                continue
            available_books -= planning.books
            plannings.append(planning)

        return BookSolution(plannings)
