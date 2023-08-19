# how to perform the slice operation in the List 
# the slice operator can be used for the deletion as well 
# while  performing the slicing we need to remember that the `first index which will be on the ledt of :` will going to be get included but the `index on the the right of the : will not be included`
# if we ignore the ` index before :` then it will start from the `beginning of the List`
# if we ignore the `index after :` then it will going to `list out the element` till the end of the list
# if we ignore the `both the first and last index before and after :` then it will print the enitre `List element`
# if we want to print the reverse of all the elements then we can do that as `::-1`

# if we want to update first 2 element then we can do that as below 

from typing import List
import string

list1:list=[chr(x) for x in range(97,103)]

print(list1)

# if we want to update the first 2 element then we can do as below 
# here we will do the List unpacking in here
list1[:2]=[chr(x) for x in range(103,105)]

print(list1[:])


# delete an element from the List in here 
# there are sevberal method to delete an element from the list 
    # we can use the `pop()` over here
    # we can use the `delete()`
    # we can use the `remove()`
    
# pop() :-

    # by default delete the `last element` in the list
    # if we want to `pop` a `specific index element` then we can use the method as `pop(<index of the element>)`
    # the pop() return the `deleted element` that been deleted from the list with or without the `index` element mentioned in there 
    # when we are popinng the `element` without providing the `index` which will delete the `last element` then the `time complexity` is of `O(1)` and space complexity is `O(1)`
    # when we are poping the `element` with the `index` number then the `element on the right need to move` hence the time complecity will be of `O(N) but space complecity will be of O(1)` as on memory nothing getting added up
    
    
list2:List[int]=[ x for x in range(6)]
print(list2.pop())
print(list2)
print(list2.pop(1))
print(list2)


# delete()
    # delete() also works like the `pop()` but based on the index , iit will not return the `removed values` like the `pop()`
    # we can delete an element by using the syntax as `del <list>[<element index>]`
    # using the delete() method uding the `slicing` we can delete `multiple element` from the list
    # to delete() the  using the syntax as `del <list>[<element index>]` is of `O(N)` as we are removing the element and replacing the `element right to it`
    # but the space complecity for the same will be of `O(1)` which is the constant space complexity

    
list3:List[str]=[ x for x in string.ascii_lowercase[:6]]
print(list3)
# eleting the element using the del() on the list as 
del list3[4]
print(list3)
del list3[1:3]
print(list3)


# remove()

    # remove() will be very useful when we know which element we want to remove 
    # we don't need to know the index of the element rather the element that we want to delete from the list in this case
    # to remove the element from the list based on the element  is of `O(N)` as we are removing the element and replacing the `element right to it`
    # but the space complecity for the same will be of `O(1)` which is the constant space complexity

list4:list=[x/1 for x in range(6)]
print(list4)
# here we can provide the element that we want to delete rather than the index of the element
list4.remove(3.0)
print(list4)


    


