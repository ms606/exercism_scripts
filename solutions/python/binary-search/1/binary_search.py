def find(search_list, value):
    current_list = search_list
    found = 0
    
    while(found == 0 and len(current_list) > 0):
        mid_index = int(len(current_list)/2)
        mid_value = current_list[mid_index]
        
        if mid_value == value:
            found = 1
        elif value < mid_value:
            current_list = current_list[:mid_index]
        else:
            current_list = current_list[mid_index + 1:]
            
    if found == 1:
        return search_list.index(value)
    else:
        raise ValueError("value not in array")