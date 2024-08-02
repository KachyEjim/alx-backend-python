#!/usr/bin/env python3
"""A python file"""
from typing import List, Tuple, Union


def zoom_array(lst: List[int], factor: Union[int, float] = 2) -> List[int]:
    """Typee annoatated function"""
    zoomed_in: List[int] = [
        item
        for item in lst
        for _ in range(int(factor))  # Convert factor to int for range
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
