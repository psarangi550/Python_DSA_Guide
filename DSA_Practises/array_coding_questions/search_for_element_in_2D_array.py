# searching an element in the 2D Array , where are going to check whether a particular value exist in the 2D array or not 
# there are many Algo Available for 2D Array but we will be looking at the linearSearch of the array in this case 
# in case of the LinearSearch goes through each element present in the 2D array and check whether the lement present or not

import numpy as np

arr1:np.array=np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])

def search2DElement(arr:np.array,target_value:int)->bool:
    
    for row_index in range(len(arr)): # here the time complecity is of O(NM)
        
        for col_index in range(len(arr[0])): # here the time complecity is of O(M) 
            
            if arr[row_index][col_index] == target_value :  # time complecity O(1) as if condition  and accessing the element is also of O(1)
                
                return True # time complecity O(1)
            
    else: # time complecity O(1)
        
        return False # time complecity O(1)
    
print(search2DElement(arr1,17))
print(search2DElement(arr1,19))

# the time complexity of the operation is of O(MN) and space complexity is of O(1)

# the linearSearch will return the first Occurances of the element as soon as it find the match it will return the value in here 
        

