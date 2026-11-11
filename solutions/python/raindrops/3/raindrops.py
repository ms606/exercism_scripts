"""Module providing a function printing python version."""

def convert(number):
    """
    Generate the sounds for matching divisors and join them together.
    Return the accumulated sounds, or the number as a string if empty.
    """
    rules = {3: "Pling", 5: "Plang", 7: "Plong"}
    
    result = "".join(sound for divisor, sound in rules.items() if number % divisor == 0)
    
    return result or str(number)
