#!/usr/bin/env python3
"""Genera una lista a partir de una comprensión asíncrona"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Recoge la lista generada async y la devuelve"""
    return [_ async for _ in async_generator()]
