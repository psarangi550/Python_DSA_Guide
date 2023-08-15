# if we want to insert an element to the start fof n array then the index 0 will be assigned to the new element and rest of the element will fgoing to shift by 1 number in this case 
# indexes of the existing element will be going to be increased by 1 number as we are inserting  new element to the start
# which is a time consuming operation 

import array 

# creating the array using the array.array() over here using python inbuild array module 

my_array=array.array("i",[1,2,3,4,5])

# we can insert method on this array to insert a new element into it at the beginning

my_array.insert(0,6)

print(my_array)


# if we want to insert the insert the element onto the middle all the rest of the element on the right must shift by one number 
# which is a time consuming operation

my_array1=array.array("i",[1,2,3,4,5])

# we can insert method on this array to insert a new element into it at the beginning

my_array1.insert(2,6)

print(my_array1)


# if we wnt to insert an element to the end pof the array then no index need to be changed onlyyya new index will going to be get created in this case

my_array2=array.array("i",[1,2,3,4,5])

# we can insert method on this array to insert a new element into it at the beginning

my_array2.insert(5,6)

print(my_array2)

# whenever we are putting the size of the array which is greater than the size of the array will be going to inser it to the end of the array

my_array3=array.array("i",[1,2,3,4,5])

my_array3.insert(6,6)

print(my_array3)

# the  time complexity of inserting an element to the array depends on the number ofelement present in the array which si of `O(N)`
# which is for the worst case scenario

# but the space complexity while inserting an element ton the array is `O(1)` in this case as we are insering only one elenment into the memory i.e one place in memory

