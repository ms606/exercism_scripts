"""Function for Sum of multiples"""

def sum_of_multiples(limit, multiples):
    """limit: Gives shows the level
       multiplies: Gives the list of achievememts 
    """
    points = 0
    unique_multiples = set()
    
    for base in multiples:
        if base == 0:
            continue
        
        for value in range(base, limit, base):
            unique_multiples.add(value)
            
    return sum(unique_multiples)
                

sum_of_multiples(10, [3, 5])