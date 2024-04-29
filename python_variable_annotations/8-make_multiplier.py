#!/usr/bin/env python3
''' Description: defines a function called make_multiplier that
takes a float multiplier as input and returns a new function that
multiplies any input float by multiplier.
    Arguments: multiplier: float
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' Return function that multiplies float by `multiplier`. '''
    return lambda x: x * multiplier
