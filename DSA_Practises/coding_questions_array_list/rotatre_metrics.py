import numpy as np

arr1:np.array=np.array([[1,2,3],[4,5,6],[7,8,9]])

# print(arr1)

# without using any functions

arr2=[]

for i in range(len(arr1)):
    result:list=[]
    for j in range(len(arr1[i])):
        result.append(arr1[j][i])
    arr2.append(result)
    
for i in range(len(arr2)):
    arr2[i]=arr2[i][::-1]
    
print(arr2)

def rotate(matrix):
    arr:list=[]
    for i in range(len(matrix)):
        result=[]
        for j in range(len(matrix[0])):
            result.append(matrix[j][i])
        arr.append(result)
        
    for i in range(len(arr)):
        arr[i]=arr[i][::-1]
        
    return arr

print(rotate(arr1))


# best approach without introducing another list

list1:list=[[1,2,3],[4,5,6],[7,8,9]]

def rotate_best(matrix):
    
    arr_length:int=len(matrix)
    
    for i in  range(arr_length): #0 #1 #2
        
        for j in  range(i,arr_length): #012 #12 #2
        
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
            #1 #1= #1 #1
            #2 #4 =#4,#2
            #3 #7 = #7 #3
            # [[1,4,7]--------->row
            # [2,5,6]
            # [3,8,9]]
            
            
            #5 #5 = #5 #5
            #6 #8 = #8 #6
            # [[1,4,7]
            #  [2,5,8]-----------> row
            #  [3,6,9]]            
            
            #9 #9 = #9 #9
            # [[1,4,7]
            #  [2,5,8]
            #  [3,6,9]]-----------> row 
             
        
    for ele in matrix:
        ele.reverse()
        
    return matrix
        


print(rotate_best(list1))

# [
    # [1,4,7]
    # [2,5,8]
    # [3,6,9]]
# ]  
# print(arr1)
                
            
                
            
    
            
            
    
    