#!/usr/bin/env python3
"""Python file"""
from typing import List, Tuple, Sequence


def element_length(lst: List[Sequence]) -> List[Tuple[Sequence, int]]:
    """A function to annotate"""
    return [(i, len(i)) for i in lst]
