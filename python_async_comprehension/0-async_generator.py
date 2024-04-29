#!/usr/bin/env python3
"""Creamos un generador"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Cada vez espera asíncronamente 1 segundo,
        luego arroja un número aleatorio entre 0 y 10"""
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
