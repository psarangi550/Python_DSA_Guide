
import numpy as np

arr1:np.array=np.array([1,2,3,4,5])

arr2:np.array=np.array([5,6,7,8,9])

def printUnorderPairs(arr1:np.array,arr2:np.array)->None:
    
    """
    
    this will help in pair two array 
        
    """
    
    for i in range(len(arr1)): #here the time complexity is of O(MN)
        
        for j in range(len(arr2)): # Here the Time complecity is of O(N)
            
            if arr1[i]<arr2[j]: # time complexity is of O(1)
                
                print(str(arr1[i])+","+str(arr2[j])) # time complexity is of O(1)
                
printUnorderPairs(arr1,arr2)

