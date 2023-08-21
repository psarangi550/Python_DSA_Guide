import numpy as np 

def reverse_array(arr:np.array):
    
    for i in range(len(arr)//2): #0 #1 #2 # here the time complecity is of O(N/2)--->O(N)
        
        other:int=len(arr)-i-1 #4 #3 #2
        
        temp:int=arr[i] # 1,2,3
        
        arr[i]=arr[other] # arr[0]=arr[4] #arr[1]=arr[3] #arr[2]=arr[2]
                          # arr[0]=5 #arr[1]=4 #arr[2]=3
                          
        arr[other]=temp # arr[4]=arr[0] #arr[3]=arr[1] #arr[2]=arr[2]
                          # arr[4]=1 #arr[3]=2 #arr[2]=3 
        
    return arr


arr1:np.array=np.array([x for x in range(1,6)])

print(reverse_array(arr1))
        
        
        