from pathlib import Path
from typing import List, Any


def as_output(file_path: Path) -> Path:
    return file_path.parent / f'{file_path.stem}_output{file_path.suffix}'


def read(file_path: Path) -> List[str]:
    with file_path.open('r') as f:
        content = f.readlines()
    content = map(str.strip, content)
    content = list(content)
    return content


def write(data: Any, file_path: Path) -> None:
    output = str(data)
    with file_path.open('w') as f:
        f.write(output)
