#!/usr/bin/env python3
"""Define una corrutina asincrona"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Espera un retardo aleatorio entre 0 y el max_delay"""
    random_number = random.uniform(0, max_delay)
    await asyncio.sleep(random_number)
    return random_number
