#!/usr/bin/env python3
''' Description: defines a function called sum_mixed_list that takes
a list of integers or floats as input and returns the sum of all
elements in the list as a float.
    Arguments: mxd_lst: List[Union[int, float]]
'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' Return sum of elements of mxd_list. '''
    return sum(mxd_lst)
