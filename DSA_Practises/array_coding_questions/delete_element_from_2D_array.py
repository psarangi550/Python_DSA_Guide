# delete the row and column from the 2D array , we can't delete the element from the 2D array then the row and column become invalid 
# deletion in 2D array will create a new array with updated dimension based on the row and column that we have deleted 

# when we delete a row or column in an `2D array` then numpy will create a New 2D array in memory `wiith the updated dimension with original value`
# this will be hgappening on the background

# the time and space complexity for the delete operation will be of O(MN) because we are copying the `remaining element` from the `original array` to the `new updated array` which creted on the memory 
# The space complecity for the delete operation is of O(MN) as we are creating a new element in the memory with updated dimention and original element

# the time and space complexity of numpy operation will be faster than the time and space complexity of the normal array due to the optimization done in the numpy module 

# in order to delete the element from the numpy 2D array we can use it as below 

import numpy as np 

arr1:np.array=np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])

# we can use the delete() on the numpy module to delete the element from the numpy array

# the below method will delete the element from the numpy array from the row 
# here the delete() takes few args of the numpy.delete()
    # existing original numpy array
    # which index of row/coulmn we want to delete 
    # what axis we want to delete o for row and 1 for column
new2Darray_row=np.delete(arr1,0,axis=0)

print(new2Darray_row)

# the below method will delete the element from the numpy array from the column as below 

new2Darray_column=np.delete(arr1,0,axis=1)

print(new2Darray_column)

