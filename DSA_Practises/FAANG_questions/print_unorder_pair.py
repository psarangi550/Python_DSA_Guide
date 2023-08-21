
import numpy as np

def printUnorderPairs(arr:np.array)->None:
    
    """
        printing the number of pair over here based on the array provided 
        
    """
    
    for i in range(len(arr)): # O(N+N-1) complexity O(N) time complexity
        
        for j in range(i+1,len(arr)): # (N-1)+(N-2)+(N-3)+.....++2+1--->O((N*(N-1))/2)===>N2/2-N/2 ===> N2 (removing the non dominant and dropping the constant over here )
            
            print(str(arr[i])+","+str(arr[j])) #O(1) complexity
            
            
arr1:np.array=np.array([1,2,3,4,5])

printUnorderPairs(arr1)

# 2nd way to find the bigO expression is of 

#---------------------------------------------------

# for the outer loop the time complecity is of O(N)

# for each iteration of the outer loop the inner loop varies from N-1...1

# for each iteration of outer loop the inner loop is of N-1 ....1 hence here we can fetch the average

# lets suppose the Inner loop run 10 times 

# for the inner loop 10,9....1 times hence we can find the average work by as 10/2 (average iteration) sum(1...10)/10=(110/2)/10=55/10=5.5 which is of 5 if we round it (average iteration)

# for N outer iteration the inner loop run n/2 times hence the time complecity is of O(N*N/2)=> O(N2/2)=>O(N2) time complecity

