# the print pair can be as below 

import numpy as np

def printPairs(array:np.array)->None:
    
    """
        printing the number of pair over here based on the array provided 
        
    """
    
    for i in array: # O(N2) complexity
        
        for j in array: # O(N) complexity
            
            print(str(i)+","+str(j)) #O(1) complexity
            
            
arr1:np.array=np.array([1,2,3,4,5])

printPairs(arr1)