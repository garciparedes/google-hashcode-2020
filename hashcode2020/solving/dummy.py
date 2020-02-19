from __future__ import annotations
from typing import List
from .abc import (
    Solver,
    Solution,
)


class DummySolver(Solver):

    @classmethod
    def from_lines(cls, raw: List[str]) -> Solver:
        return DummySolver()

    def solve(self) -> DummySolution:
        return DummySolution()


class DummySolution(Solution):
    def __str__(self) -> str:
        return 'dummy'
