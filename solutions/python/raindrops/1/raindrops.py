def convert(number):
    isDivisible3 = ''
    isDivisible5 = ''
    isDivisible7 = ''

    if number % 3 == 0:
        isDivisible3 = 'Pling'
    if number % 5 == 0:
        isDivisible5 = 'Plang'
    if number % 7 == 0:
        isDivisible7 = 'Plong'   

    if len(isDivisible3) + len(isDivisible5) + len(isDivisible7) == 0:
        return str(number)
        
    return isDivisible3 + isDivisible5 + isDivisible7
                