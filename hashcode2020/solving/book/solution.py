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
        raw_result = list()
        raw_result.append(f'{len(self.plannings)}')

        for planning in self.plannings:
            raw_result.append(f'{planning.identifier} {len(planning.books)}')
            raw_result.append(' '.join(map(str, planning.book_identifiers)))

        result = '\n'.join(raw_result)
        return result

    @property
    def score(self) -> int:
        return sum((planning.score for planning in self.plannings), 0)
