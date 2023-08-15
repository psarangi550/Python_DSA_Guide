# accessing the element means print the value present in the cell 
# for each space in the memory the index value increses as `1`

from array import *

arr1=array("i",[1,2,3,4,5,6])

def accessEelement(arr:array,index:int)->None:
    
    if index >= len(arr) : #here the time complecity is of O(1)
        
        print("There is No Element Located in %s with %d" %(arr, index))  #here the time complecity is of O(1)
        
    else: #here the time complecity is of O(1)
        
        print(arr1[index]) #here the time complecity is of O(1) because we are accessing one element from the array 
        
accessEelement(arr1,5)
accessEelement(arr1,7)
accessEelement(arr1,6)

# in total the  time complecity is of O(1)
# as we are accessing the one element which is already being stored to the memory hence its also a constant space complecity which is of O(1) space complexcity
# hence new memory location is not need in this case

