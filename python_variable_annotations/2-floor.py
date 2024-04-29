#!/usr/bin/env python3
''' Description: defines a Python function called floor
that takes a single float argument n and returns the
largest integer value less than or equal to n. The function
is annotated with the return type int.
    Arguments: n: float
'''


def floor(n: float) -> int:
    ''' Return the largest int value less than or equal to n. '''
    return int(n) if n >= 0 else int(n) - 1
