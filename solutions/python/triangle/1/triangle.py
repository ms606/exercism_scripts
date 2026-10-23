def isValidTriangle(sides):
    a, b, c = sides
    if (a <= 0 or b <= 0 or c <= 0):
        return False
    return (a + b >= c) and (b + c >= a) and (a + c >= b)
    
def equilateral(sides):
    a, b, c = sides
    return (isValidTriangle(sides) and (len(set(sides)) == 1) and (a == b == c)  )

def isosceles(sides):
    a, b, c = sides
    return (isValidTriangle(sides) and (len(set(sides)) <= 2))


def scalene(sides):
    a, b, c = sides
    return (isValidTriangle(sides) and (len(set(sides)) == 3))
