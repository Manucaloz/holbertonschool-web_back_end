#!/usr/bin/env python3
"""Tiempo de medición"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Ejecuta async_comprehension cuatro veces en paralelo y
    measure_runtime debería medir el tiempo de ejecución total y devolverlo"""
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    return time.perf_counter() - start_time
