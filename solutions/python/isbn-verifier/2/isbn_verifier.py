def is_valid(isbn):
    isbn_cleaned = isbn.replace("-", "")
    
    if len(isbn_cleaned) != 10:
        return False
        
    result = 0
    d = 10
    
    for index, char in enumerate(isbn_cleaned):
        if char == "X":
    
            if index == 9:
                num = 10
            else:
                return False
        elif char.isdigit():
                   num = int(char)        
            
        else:
    
            return False
            
        result += num * d
        d -= 1  
        
    return result % 11 == 0