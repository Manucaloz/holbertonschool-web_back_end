#!/usr/bin/env python3
''' Description: defines a function called element_length that takes an
iterable of sequences (e.g. lists, tuples) as input and returns a list
of tuples, where each tuple consists of an element and its length.
    Arguments: lst: Iterable[Sequence]
'''

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Return list of tuples, one for each element, of which
       consists of the element itself and its length.
    '''
    return [(i, len(i)) for i in lst]
