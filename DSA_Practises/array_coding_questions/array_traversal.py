# traversing means visiting all cell of the array elements untill the end 

# this can be due to 
    # print each number 
    # updating a specific number 

# we can create the loop and start from the sequencial order for traversing 

# we can create an array of decimal number using it as 

from array import * #importing all attribute and function from array module

my_decimal_arr=array("d",[1.3,1.5,1.6])

# print(my_decimal_arr)

def traverArray(arr:array)->None:
    
    for ele in arr:
        print(ele)
        
        
traverArray(my_decimal_arr)

# the time and space complexity for the below operation is of O(N) and printing is fo O(1) as we can drop the non dominant complecity hence it will be of O(N)

# as we don't want the new space rather just tio iterate over the same hence the space complexity of the same is of O(1)


        
    
    