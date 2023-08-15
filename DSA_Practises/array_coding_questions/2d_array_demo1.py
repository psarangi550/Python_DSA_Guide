# Creating 2D Array using python 

# 2D Array is a combination of 1D Array
# There can be multiple rows (which represent a 1D array) while declariong the 2D Array in this case 
# in case of the 1D array we have single row with multiple columns inside of it 

# But in case of we can multiple row and each row can have multiple columns
# In case of the Metrix we need to use the 2D Array to plot the visula environment of the game 
# ex:- consider we are recording the temperature 4times a day for 4 days , for each day we are recording the temperature 4 times a day, for this we need to use the 2D Array

# we need  to access the element by using the a[i][j]


# while define the 2D Array we need to define the below things

# we need to define the veriable 
# define the TYPE of array we want to represent
# we need to define the size of the 2D Array in here 

# here we need to use the `numpy` module to define the `2D Array` in this case


# Day1:- 11, 15, 10, 6
# Day2:- 10, 14, 11, 5
# Day3:- 12, 17, 12, 8
# Day4:- 15, 18, 14, 9

import numpy as np

two_dimentional_array:np.array =np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])

print(two_dimentional_array)

# the time complexity of creating the 2D array is O(MN) and also the space complexity is of O(MN)
# where the `M` is the number of columns and the `N` is the number of `rows`


# different operation that can be performed on a 2D Array 

# insertion value into the 2D array can be done by using the below concept 


# we can't insert a sing;e value to the 2D array but rather we need to add a row and column 
# we can't insert one value into the 2D array as rest of column and row can't be empty then it can be consider as the `One Dimentional Array` , but the 2D Array shoulod be in the Metrix Format
# there are 2 ways to add the values onto the 2D Array which is of 
    # addition of column 
        # when we add a new column to the existing column the existing column need to be moved to the new column
        # here the time complexity of the operation is of `O(MN)` where `M` no of column and `N` is the number of rows
        # here when shifting we need to shift the `N` number of element present in the row upto `M` column in order to adjust the new column
        
         
    # addition of row 
        # the time complexity of this operation will also be of `O(MN)` where `M` is the number of `column` and `N` is the number of `rows`
        # when we add the new row to the existing 2D array then we need to move the `M` number of elements present in the column to the `N` rows that is present




# for inserting a value into the existing element we need to use the `np.insert()` which takes args auch as 
    # existing array 
    # location of columns and rows where we want to add the new values
    # elements that we want to add to the column 
    # in which position we want to add and element that we want to add can be mentioned in here here 0 represents the rows in this case  which can be set alongisde the axis `keyword args` as below 
    # here in the above one axis `0` means rows and `1` means column  as we are adding the column we can mention that as `axis=1`  

new_2d_array_column=np.insert(two_dimentional_array, 0,[[1,2,3,4]],axis=1)

# print(new_2d_array_column)  # here the elements were added the new column shifting all the existing element in the row to the `M` columns

# similarly if we want to add the row in this case we can represent as below 


new_2d_array_row=np.insert(new_2d_array_column, 0,[[5,6,7,8,9]],axis=0)

# print(new_2d_array_row) 


# if we want to add the 2nd row as `[9,10,11,12]` then we can represent that using

new_2d_array_row_pos2=np.insert(two_dimentional_array, 1,[[9,10,11,12]],axis=0)

# print(new_2d_array_row_pos2)


# there is additional method which can add `row/column` to the `2D Array` at the end as below 
# here we can use the append() method to the `np` module to insert a row or column on to the last of the array 
# the np.append() also takes few arguments
    # here we need to provide the existing numpy array to which we want to append 
    # we also have to provide the values that we want to add
    # then we need to provide the axis which si for Row is of `0` and fpor column is of `1`


new_append_array_row=np.append(two_dimentional_array,[[1,2,3,4]],axis=0)

# print(new_append_array_row)

# while adding to the column we can use it as below

# Create the new column to be added
new_column = np.array([1, 2, 3, 4])

# Use numpy.append() to add the new column to the existing array
new_array = np.append(two_dimentional_array, new_column.reshape(-1, 1), axis=1)

print("Existing Array:")
print(two_dimentional_array)
print("\nNew Column:")
print(new_column)
print("\nNew Array with Added Column:")
print(new_array)


