# similarity between List and Array 

    # Both the List and Array Data Structure are mutable in nature 
    # Both can be indexed and can be iterated through 
    # by uisng the index we can modify the value in the array as they are mutable in nature 
    # Both of them can be sliced as well 
    
# Difference between the List and Array Data Structure

    # the operation that can be performed on both the List and Array Data Structure
    # Arrays are used for strong arthimatic calculation or computation
    # In Array we have to store the homogenious item where as on the list we can store the hetrogenious item
    # when we putt the array with `multiple type` such as `int and str` then that will be converted into `one type` , ex when we put the `str and int` it will convert to `str` type 
    
    
import numpy as np 

from typing import List

arr1:np.array=np.array([1,2,3,4,5,6])

list1:List[int]=[1,2,3,4,5,6]

# we can perform the divide operation on the Array which will be performed for each element on the Array 
# but we can't perform such operation on the List

new_arr:np.array=arr1/2

# but we can't perform such as list1/2 for the arithmatic operation which is of TypeError 

print(new_arr)


# when we put a string and int mix then the integer also being converted to the string elements 
# here as we are putting the string element over here hence that will be converted to the String element
arr2:np.array=np.array([1,2,3,4,5,6,'a'])
print(arr2)

