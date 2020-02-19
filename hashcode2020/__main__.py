from __future__ import annotations

import sys
from pathlib import Path

from .solving import (
    DummySolver,
)
from .io import (
    read,
    write,
    as_output,
)


def main():
    input_file_path = Path(input('Type the input file path:') if len(sys.argv) < 2 else sys.argv[1])
    output_file_path = as_output(input_file_path)

    input_data = read(input_file_path)

    solver = DummySolver.from_lines(input_data)  # TODO: Replace by "DummySolver" by real implementation.
    solution = solver.solve()

    write(solution, output_file_path)


if __name__ == '__main__':
    main()
