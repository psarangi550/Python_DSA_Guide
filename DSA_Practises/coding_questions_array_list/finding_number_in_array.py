# finding an element in the array 
# in python there were no inbuilt method for searching an element  like `in` operatior in `List`

import numpy as np

arr1:np.array=np.array([x for x in range(1,21)])

def fetchElement(arr:np.array,element:int)->str:
    
    for i in range(len(arr)):
        
        if arr[i]==element:
            
            return (f"Element {element} Found at index {i}")
            
    return(f"Element {element} Not Found in Array {arr}")
    
print(fetchElement(arr1,16))
print(fetchElement(arr1,21))
