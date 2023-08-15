# here we need to access all element/cell inside the 2D array
# this can be due to updating a specific element or accessing a specific element and printing them 
# here we need to traverse through ROW and COLUMNS over here 
# when we are printing the element then we first print element based on the row wise then we are going to the next column and perform the same operation 
# hence the for loop below we need to go for each row and fetch the element in each column and then go for the next column

# if `M` is the `Number of column`  and `N` is the `Number of Rows` then  

import numpy as np 

arr1:np.array=np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])

def traverse2DElement(arr:np.array)->None:
    
    for row_index in range(len(arr)): # here while comparing the row we don't have to consider the index as the 2D array length by default provide the lenght of the array
        
        # the time complexity is of O(NM) because for each row we need to traverse all the `M` element in the column 
        
        for column_index in range(len(arr[0])): #here we need to take the range of arr[0] cause we are know the number of columns in here 
            
            # the time complexity id of O(M) #here we need to traverse the one row at a time hence the it will be of O()
            
            print(arr[row_index][column_index]) #here the time complecity is of O(1)
            
        print() #here the time complecity is of O(1)

traverse2DElement(arr1)   
 
# space and time complexity will be of O(MN) for traversing but the space complexity will be O(1)

# if the Number of row and the number of column being the same then it will be of quadratic time complexity which will be of O(N2)

