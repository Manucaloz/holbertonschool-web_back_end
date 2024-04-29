#!/usr/bin/env python3
"""Se ejecuta varias corrutinas al mismo tiempo con async"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Se genera un wait_random n veces con el max_delay especificado
    y devuelve la lista de todos los retardos (float)."""
    futures = [wait_random(max_delay) for _ in range(n)]
    futures = asyncio.as_completed(futures)
    delays = [await future for future in futures]
    return delays
