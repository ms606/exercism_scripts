def sum_of_multiples(limit, multiples):
    points = 0

    
    for mul_points in range(1, limit):
        print (mul_points, 'mul_points')
        
        for multiple in multiples:
            print (multiple, mul_points,'multiple')
            if multiple == 0:
                continue
                
            if mul_points % multiple == 0:
                points += mul_points
                break 
                
    return points
                

sum_of_multiples(10, [3, 5])