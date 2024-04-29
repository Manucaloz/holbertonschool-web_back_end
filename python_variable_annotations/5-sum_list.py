#!/usr/bin/env python3
''' Description: defines a Python function called sum_list that takes a
list of floating-point numbers as input and returns the sum of all
elements in the list.
    Arguments: input_list: List[float]
'''

from typing import List


def sum_list(input_list: List[float]) -> float:
    '''Return sum of all elements in input_list. '''
    return sum(input_list)
