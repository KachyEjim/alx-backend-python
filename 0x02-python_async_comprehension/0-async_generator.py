#!/usr/bin/env python3
"""Python file"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None]:
    """Yield a random flaot between 0 and 10 when called"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
