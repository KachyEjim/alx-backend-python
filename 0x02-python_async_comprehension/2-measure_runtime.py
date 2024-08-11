#!/usr/bin/env python3
"""Python file"""

import time
from asyncio import gather

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Mesure the total runtime"""
    start_time = time.perf_counter()

    await gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )

    end_time = time.perf_counter()
    return end_time - start_time
