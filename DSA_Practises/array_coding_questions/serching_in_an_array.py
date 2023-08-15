# search in Array can be performed using the `linearSearch algorithm `
# in LinearSearh we need to search each element of the array to the target value
# if the match found then we can return the index of the matched element or target value 
# if not match not found then in that case search is unsuccessful and we can output the result as per the wish 

from array import *
from typing import Union

arr1=array("i",[1,2,3,4,5,6])

# here we need to perform the linear search for getting the elements of the array

def searchElementUsingIndex(arr:array, target)->Union[int,str]:
    
    for index in range(len(arr)):  # here  the time complexity for the for loop is of O(N)
        
        if arr[index]==target: # for the if statement the time complecity is of O(1)
            
            return index  # return also a constant time complecioty hence the time complecity is of O(1) in here 
    else:  
        return "No match found" # here insted of the str we can also return -1 which means the elements not found in here 
    
        # here also for this the time complecity is of O(1)
        
# hence the total time complxity will be of O(N) in this case 

# the time complexity of len() is of O(1) which is the constant time complecity 

# the time complexity of the range() is also of O(1) as it does not create the actual sequence of interger same as the array , but rather create a iterator object which is of range object 
# which can be produced on demand based on the length of the Array

# the space complecity of the function will be of O(1) as we are just accessing the element of array which is already created  we are not changing the value 


def searchElementUsingElement(arr:array, target)->Union[int,str]:
    
    for ind in arr:
        
        if ind==target:
            
            return arr.index(ind)  
    else:  
        return "No match found"
    

# print(searchElementUsingIndex(arr1,5))
# print(searchElementUsingIndex(arr1,9))


print(searchElementUsingElement(arr1,5))
print(searchElementUsingElement(arr1,9))

