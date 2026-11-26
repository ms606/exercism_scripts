"""Functions implementing common list operations."""


def append(items1, items2):
    """Combine two lists."""
    return items1 + items2


def concat(lists):
    """Flatten a list of lists."""
    return [item for sublist in lists for item in sublist]


def filter(function, items):
    """Return items that satisfy the given function."""
    new_list = []
    for item in items:
        if function(item):
            new_list.append(item)
    return new_list


def length(items):
    """Count the number of items."""
    count_item = 0
    for item in items:
        count_item += 1
    return count_item


def map(function, items):
    """Apply a function to every item."""
    return [function(item) for item in items]


def foldl(function, items, initial):
    """Fold items from left to right."""
    accumulator = initial
    for item in items:
        accumulator = function(accumulator, item)
    return accumulator


def foldr(function, items, initial):
    """Fold items from right to left."""
    accumulator = initial
    for item in reversed(items):
        accumulator = function(accumulator, item)
    return accumulator


def reverse(items):
    """Return items in reverse order."""
    return items[::-1]