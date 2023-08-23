# insert and update the new key-value pair onto the dictionary 

# as dictionary are `mutable`` in nature hence we can add the `new element` or update the `existing element` using the `assignment operator`
# if the `key` alreadty present the existing value wil going to be get updated else if the keey is not present then the `key and value` added as a new entry to dictionary

from typing import Dict,Union


myDict:Dict[str,Union[str,int]] = {"name":"pratik","age":26}

# we can update the value as below 

myDict["name"]="Edy"

print(myDict)

# the time complexity of updating the `dictionary element` is of `O(1)` complexity
# as we are accessing the dictionary `values` based on the `key` and `if the key already present` then updating the `values`
# the space complexity for the same is of `O(1)` as we don't need the additional space for the same 

   
# inserting also value can also be done using the assignment operator where it will be checking key is present or not if not present then add both the key-value pair as new entry 
# the time complexity of for adding the element to the dictionary is of `O(1)` as we are adding one element i.e `key-value` to the dictionary
# the space complexity for adding an `key-value` pair is of `amortized O(1)`
# for most of the case when we add the primitive data structure is `O(1)`
# but that can change to `O(N)` based the underlying `DS of key-value` grow or shrink
# if we add the `key-value` to the `dictionary` and thee `dictionary linit being reached` the `dict object will required the double the size in that case the space complexity is of O(1)`



myDict["city"]="bangalore"

print(myDict)

