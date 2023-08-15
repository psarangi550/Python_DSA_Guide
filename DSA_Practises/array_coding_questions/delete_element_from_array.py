# delete an element from the array 

# when we delete the element from an array that element must be present in the array 
# once the element is being deleted the `there will not be any free space` rather we can `be occupied by the next element` keeping the `last cell` as empty
# if we are keeping the space as empty then we are loosing the efficiency of `contguous memory location` which will help in the `ranmdom access of the element in the array using the index`


# deletion will become efficient when we delete the large number of element welse it will be a time consuming process 


from array import *

arr1:array=array("i",[1,2,3,4,5,6])

# here we can call the remove(<value of the element>) on the array object inorder to remove an value from the array 

arr1.remove(1)
arr1.remove(5)

# the space and time complecity of the functiuon will be of O(1) and O(N)

# if we are removing the last element is of O(1) , as we are `removing element by provioding the element` and `no replacing  is going to happen`

# when we delete an element in the beginning or in the middle then we can see that both the `removal of element and replacement of the element also happened` which is of O(N)

print(arr1)