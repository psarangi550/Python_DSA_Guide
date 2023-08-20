def contain_duplicate(arr:list):
    
    for ele in arr:
        
        if arr.count(ele)>1:
            
            return True
    
    return False

print(contain_duplicate([1,2,3,1]))
print(contain_duplicate([1,2,3]))


# best approach using the list and set as below 

def best_contain_suplicate(arr:list):
    
    seen=set()
    
    for ele in arr:
          
        seen.add(ele)
            
    if len(seen)==len(arr):
        
        return False
    
    else:
        
        return True

print(best_contain_suplicate([1,2,3,1]))
print(best_contain_suplicate([1,2,3]))


# another approach

def best_contain_duplicate(arr:list):
    
    seen=set()
    
    for ele in arr:
        
        if ele in seen:
            
            return True
          
        seen.add(ele)
        
    return False

print(best_contain_duplicate([1,2,3,1]))
print(best_contain_duplicate([1,2,3]))
            
    
            
    