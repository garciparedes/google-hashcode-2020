from __future__ import annotations

from typing import (
    List,
    Set,
    Tuple,
    Union,
    Iterable,
)

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

    def library_potential(self, library) -> Tuple[Union[int, float], ...]:
        return library.books_per_days * library.available_score / library.signup_days ** 2,

    def sort_libraries(self, libraries: Iterable[Library]):
        return sorted(libraries, key=lambda x: self.library_potential(x), reverse=True)

    def solve(self) -> BookSolution:
        sorted_libraries = self.sort_libraries(self.libraries)

        available_days = self.available_days
        available_books = set(self.books)

        plannings = list()
        for library in sorted_libraries:
            planning = LibraryPlanning(library)
            planning.insert_possible_books(available_books, available_days)
            if not any(planning.books):
                continue
            available_days -= library.signup_days
            available_books -= planning.books
            plannings.append(planning)

        solution = BookSolution(plannings)
        print(solution.score)
        return solution
