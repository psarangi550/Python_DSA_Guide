
# best approach

def best_score(arr1:list)->tuple:
    
    max1,max2=0,0
    
    for ele in arr1:
        
        if ele>max1:
            max2=max1
            max1=ele
        elif ele>max2:
            max2=ele
            
    return max1,max2

print(best_score([84,85,86,87,85,90,85,83,23,45,84,1,2,0]))

    
    

