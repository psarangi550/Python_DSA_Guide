def maxIntegerProduct(arr:list):
    
    max1,max2=0,0
    
    for num in arr:
        
        if num > max1:
            max2=max1 # 0 # 1 #7
            max1=num # 1 # 7 # 9
        
        elif num>max2: # 3> 1,4>3
            max2=num # 3 # 4
            
    return max1*max2

print(maxIntegerProduct([1, 7, 3, 4, 9, 5]))
    