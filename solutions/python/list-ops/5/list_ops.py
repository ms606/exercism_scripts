def append(list1, list2):
    """Functions for performing append operations."""
    return list1 + list2

def concat(lists):
    """Functions for performing concat operations."""
    return [item for sublist in lists for item in sublist]

def filter(function, items):
    """Functions for performing filter operations."""
    new_list = []
    for item in items:
        if function(item):
            new_list.append(item)
    return new_list

def length(lists):
    """Functions for performing length operations."""
    count_item = 0
    for list in lists:
        count_item += 1
    return count_item

def map(function, list):
    """Functions for performing map operations."""
    return [function(item) for item in list]

def foldl(function, list, initial):
    """Functions for performing foldl operations."""
    accumulator = initial
    for item in list:
        accumulator = function(accumulator, item)
    return accumulator

def foldr(function, list, initial):
    """Functions for performing foldr operations."""
    accumulator = initial
    for item in reversed(list):
        accumulator = function(accumulator, item)
    return accumulator

def reverse(list):
    """Functions for performing reverse operations."""
    return list[::-1]
