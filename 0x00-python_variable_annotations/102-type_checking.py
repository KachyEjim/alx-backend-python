#!/usr/bin/env python3
"""A python file"""
from typing import Tuple, List, Union


def zoom_array(lst: Tuple[int, ...], factor: Union[int, float] = 2) -> List[int]:
    if not isinstance(factor, int):
        factor = int(round(factor))  # Convert factor to integer

    zoomed_in: List[int] = [item for item in lst for _ in range(factor)]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
