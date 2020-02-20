from __future__ import annotations
from typing import List

from ..abc import Solution
from .models import (
    LibraryPlanning
)


class BookSolution(Solution):
    def __init__(self, plannings: List[LibraryPlanning]):
        self.plannings = plannings

    def __str__(self) -> str:
        result = str()
        result += f'{len(self.plannings)}\n'

        for planning in self.plannings:
            result += f'{planning.identifier} {len(planning.books)}\n'
            result += ' '.join(map(str, planning.book_identifiers)) + '\n'
        return result
