#!/usr/bin/env python3
''' Description: defines a function called to_kv that takes two arguments,
k of type str and v of type int or float, and returns a tuple containing
the key-value pair (k, v^2).
    Arguments: k: str, v: Union[int, float]
'''

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' Return tuple consisting of k and the square of v. '''
    return (k, v * v)
