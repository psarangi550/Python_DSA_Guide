# how to access any given any cell in the 2D array uisng the numpy module 
# the one dimentional array starts from 0 and their value increases by 1 when we are going in the column value 
# but in case of the 2D array we have 2 indexes where 1st represent the `row index` and 2nd represent the `column index`
# here for both the `row index` and `column index` starts from the 0
# we can access the element using the conmcept as `<array name>[<row index>][<column index>]`

import numpy as np

from typing import Union

arr1:np.array=np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])

# when we print the lenght of the array then that will provide the length of the `row` i.e the number of rows

print(len(arr1))

# if we want to know the length of the column then we can get by using the `len(<2D array>[0])`

print(len(arr1[0]))

def access2DElements(arr:np.array,row_index:int,column_index:int)->Union[int,str]:
    
    if row_index >= len(arr) or column_index >= len(arr[0]): # here the time complecity as O(1)
        
        return "Element at row_index %d and column index %d Not Found for Array %s" % (row_index,column_index,arr) # here the time complecity as O(1)
    
    else: # here the time complecity as O(1)
        
        return arr[row_index][column_index] # here the time complecity as O(1)
        
    

print(access2DElements(arr1,2,2))

# the time and space complecity over here overall is of O(1)

# accessing the elements from the 2D array Takes O(1) time complecity and space complecity is aslo of O(1) as we are not adding the element over here 


        
