"""We need to flatten the list and nested collection, using recursive logic"""

def flatten(iterable):
    """iterable: list + nested list"""
    result = []
    for item in iterable:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        elif item is not None:
            result.append(item)
    return result