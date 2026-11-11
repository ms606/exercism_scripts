def append(list1, list2):
    return list1 + list2

def concat(lists):
    return [item for sublist in lists for item in sublist]

def filter(function, list):
    new_list = []
    for item in list:
        if function(item):
            new_list.append(item)
    return new_list

def length(list):
    count_item = 0
    for _ in list:
        count_item += 1
    return count_item

def map(function, list):
    return [function(item) for item in list]

def foldl(function, list, initial):
    accumulator = initial
    for item in list:
        accumulator = function(accumulator, item)
    return accumulator

def foldr(function, list, initial):
    accumulator = initial
    for item in reversed(list):
        accumulator = function(accumulator, item)
    return accumulator

def reverse(list):
    return list[::-1]
