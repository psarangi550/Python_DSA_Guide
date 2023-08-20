

def remove_duplicates(arr:list):
    
    new_set=set(arr)
    
    return list(new_set)

print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))


# best approach for this will be off as below 

def remove_dup_element(arr:list):
    
    unique_list=[]
    
    seen:set=set()
    
    for item in arr:
        
        if item not in seen:
            
            unique_list.append(item)
            seen.add(item)
            
    return unique_list


print(remove_dup_element([1, 1, 2, 2, 3, 4, 5]))
    

