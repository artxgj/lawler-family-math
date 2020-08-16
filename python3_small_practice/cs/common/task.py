from dataclasses import dataclass
from typing import Union, Any


@dataclass
class Task:
    start: Union[float, int]
    finish: Union[float, int]
    weight: Union[float, int] = 1
    id: Any = None
