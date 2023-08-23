# there are various way to delete an element i.e the key-value pair from the dictionary 

    # we can use the `del` keyword with the dictionary and its key which can remove the pair  of key and value 
    # we can also use the pop() which will return the value of the key from the dictionary which is getting deleted 
    # we can also use the popitem() which will `remove and return the last inserted key` from the dictionary
    # before python 3.7 if we are using the popitem() will delete the random element from the dictionary
    # but after pythton 3.7 if we are using the popitem() which will `remove and return the last inserted key` from the dictionary
    # we can also iuse the clear() to remove all the elements from the dictionary make it as empty dictionary 
    
    
from typing import Dict,Union

mydict:Dict[str,Union[str,int]]=dict(name="Edy",age=26,address="bangalore")

del mydict["age"]

print(mydict)


# the time complecity to delete an element i.e the key-value pair from the dictionary is of `O(1)` as it involve the `O(1)` as it involvb hash table operation
# the space complecity to deletean element i.e the key-value pair from the dictionary is of `O(1)` as no additional memory required for this 


from typing import Dict,Union

mydict:Dict[str,Union[str,int]]=dict(name="Edy",age=26,address="bangalore")

# the pop() will return a default value if the key is not found in the dictionary
# we can pass a default value that need to be return if the key not found in the dictionary 
# if we are not providing the default value and the key not found that case we will be getting the KeyError instead
# it is always recomended to provide the default value while using the pop() function


returned_value:Union[str,int]=mydict.pop("address1","Not Found")

print(mydict)

print(returned_value)

# the time and space complexity for the `pop()` will be off O(1) as its fetch the element and delete that specific element as it involvb hash table operation
# also the space complexity for the same is also off `O(1)` as we don't need additional space for the same


# the popitem() will remove and return the key-value as tuple as an outcome which been inserted at the end 
# in case of the pop() we are getting the value as the return but in case of the popitem we will be getting the key-value pair as the tuple in return 

myDict:Dict[str,Union[str,int]]=dict(name="Edy",age=26,address="bangalore")

print(myDict.popitem())

print(myDict)


# the time and space complexity for the `popitem()` will be off O(1) as its fetch the element and delete that specific element as it involvb hash table operation
# also the space complexity for the same is also off `O(1)` as we don't need additional space for the same


# the clear() will empty the dictionary but will not return anything in return same as the del keyword 

myDict:Dict[str,Union[str,int]]=dict(name="Edy",age=26,address="bangalore")

myDict.clear()

print(myDict)


# the time complecity for the same will be of O(N) where `n` is the number of element in the dictionary i.e the key-value pair 
# the space complecity wil be of O(1) as no extra memory space being needed for the same 