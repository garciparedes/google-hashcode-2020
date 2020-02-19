from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List


class Solver(ABC):

    @classmethod
    @abstractmethod
    def from_lines(cls, raw: List[str]) -> Solver:
        pass

    @abstractmethod
    def solve(self) -> Solution:
        pass


class Solution(ABC):

    @abstractmethod
    def __str__(self) -> str:
        pass
