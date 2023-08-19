# pitfall of the list and how to avoid them

# most of the list method modify the argument and return nothing hence we should't use them directly 
# but when we apply the same to the string then it will create a new string as they are immutable in nature

# there are multiple ways to do the same thing 
# we  can do the same thing for delete the element from the list 

    # pop()
    # delete()
    # remove()
    # slicing assignments
    
# when we are performing any operation on the list that can modify the same list as they are mutable in nature 
# But in order to avoid that we can take a copy of the list before performing any operation on the same 
# we can use the copy of the list using below 2 method

    # by using list slicing 
    # by suing the copy() method from copy module in here 
    
from typing import List
from copy import copy
    
list1:List[int]=[x for x in range(6,-1,-1)]

org_list:List[int]=list1[:]

org_list2:List[int]=copy(list1)

list1.sort()

print(list1)

print(org_list)

print(org_list2)

# but when we use the python in build sorted() then that will create a New Python List instead of modifying the same List


    
