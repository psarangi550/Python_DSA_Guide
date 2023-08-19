#  if we want to update and insert element into the list that can be done as list are mutable in nature
#  list are `mutable data structure` hence we can `change the order of the elements in the list`
#  `due to this mutablity` we can also` reassign a element with a new value` in the list 
#  when the bracket appear on the `left hand side` that means we are assigning a value into the `list element identified by the bracket operator having index inside of it`


# the time and space complexity to update the element is of `O(1)` as extra memory space not required and time complexity is of O(1) complecxity

# while inserting a value onto the list we can consider the below things 

    # inserting the element at the beginning of the list # for this we need to use the insert() of the list # time and space complexity is of O(N) and O(1)
    # inserting the elemnt to any given space in the list # for this we need to use the insert() of the list # time and space complexity is of O(N) and O(1)
    # inserting the element to the end of the list # here we need to use the append() of the list  # here the time and space complecity is of O(1)
    # inserting one list into another list as individual element # here we need to use the extend() of the list # here the time and space complexity is of O(N)     
    
# while using the extend() the order of the array that we weant to add wil going to be get preserved in here 
    
