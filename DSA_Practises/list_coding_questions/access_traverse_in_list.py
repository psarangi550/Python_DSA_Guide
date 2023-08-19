# the Memory Management for the Accessing the Element and Travesing the List Element will be similar as the Array 
# the syntax of Accessing the List is similar to the syntax of an array element

from typing import Union,Any

def accessListElement(list1:list,index:int)->Union[int,str]:
    
    if index >= len(list1) :
        
        return "Element Not Present in %s for in index %d " %(list1,index)
    
    else:
        
        return list1[index]
    
    
list2:list=[1,2.5,"read",[2.5,3.5],["test"]]

print(accessListElement(list2,3))
print(accessListElement(list2,7))


# the relationship between the index and list element which is of `mapping type`
# each index map to one of the `array element` mentioned in here 
# any interger expression can be considered as the index element
# we can also access the list element by using the `in` membership operator as
# by using the index we are actually checking whether the element being present or not 
# here the time and space complecity for accessing the list element is of O(1) and space complecity is of O(1)


# with the `negetive index` we can access the lst value of the element
# when we come from backward then it starts from the `-1` value going until the `-(len(list))`
# when we are using the len() then the last element can't be accessed , hence we need to use the range() along with the `len()` for not counting in the lst value as the range() works for `0 to n-1`

# we can traverse through the empty List as well but this seems highly unlikely
# when we traverse through the empty list nothing will be going to get printed out i.e inside the for loop


def accessListElementMember(list1:list,elem:Any)->Union[int,str]:
    
    for ele in list1 :
        
        if ele==elem:
            
            return ele
        
    return "Element %.1f not present in List %s" %(elem,list1)
        
print(accessListElementMember(list2,2.5))
print(accessListElementMember(list2,3.5))


def traverseListElement(list1:list)->None:
    
    for index in range(len(list1)):
        
        print(list1[index],end=",")
        
traverseListElement(list2)

# if we use the for loop then we want to perform the operation on the `List Element` then we can use the `range(len(list))` in order to perform some action on it 


# here the time and space complecity for the traversing the Element in the List is of O(N) and space complecity is of O(1)


