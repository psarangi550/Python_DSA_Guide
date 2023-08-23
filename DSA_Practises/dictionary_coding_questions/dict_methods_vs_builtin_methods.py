# dictionary method in built in methods 

# we can use the `in and not in` operator to check whhether the key being present in the dictionary or Not 
# if we want to use the `values()` with the `in  or not in operator` to check whether the  value of a key being present in the dictionary or not

       
from typing import Dict,Union 

myDict:Dict[str,Union[str,int]]={"name":"pratik","age":26,"address":"banagaloe"}

print("pratik" in myDict.values())


# Builtin function which can be used with the dictionary 

    # len():- it will consider the number of element i.e the key-value pairs in the dictionary
    
    # all() :- if all the key here are `True` then the all() function will return True as the outcome 
        # if we have a `dict with key value as 0` then all() will return as Flase as the `O` in python means `False`
        # when we have all the `keys` as True then it will return the value as True over here 
        # but if all the `Keys` are of `False` then it will return the value as `False` 
        # if the Keys are the mix of `True and False` then also in that case it will return False in response  
        # if one key is `False` and rest are of `True` then also it will return the value as `False` 
    
    # any():-
        
        # there are 4 cases for the any() function as well 
        # if all the value of the keys are of True then it will return True in response
        # if any of the Key being True then also it will return True 
        # if one Key being False rest all are True then in that case also we will get the return value as `True`
        # if we got the all the Key being False then in that case it will return the value as `False` 
    
    
    # sorted():-
        # by using the sorted() on the list we can get a new list with values sorted in natural sorting order
        # but when we use the sorted() on the dictionary we will be getting the List of keys in the sorted manner in natural sorting order 
        
        
    
    
    
    
    