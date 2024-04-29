#!/usr/bin/env python3
"""Se ejecutan varias corrutinas al mismo tiempo con async"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Genera wait_random n veces con el max_delay especificado
    y devuelve la lista de todos los retardos (float).."""
    futures = [task_wait_random(max_delay) for _ in range(n)]
    futures = asyncio.as_completed(futures)
    delays = [await future for future in futures]
    return delays
