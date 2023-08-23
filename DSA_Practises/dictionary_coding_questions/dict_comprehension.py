# we can also perform the dict comprehension same as list comprehension

# this will help in creating the new dict based on the existing dictionary object or any Sequence of key-value pair  or any iterable of  Key-value pair

# the syntax for the same can be written as below 

#    { new_key:new_value for item in list}

# if we want to include the if consition then we can write as below 

#    { new_key:new_value for item in list/sequence if condition }

from typing import Dict,List

import random

dist1:Dict[int,int]={x:10 for x in range(10)}

print(dist1)

# we can also make a fresh dict from the values of the existing dict object

city_names:List[str]=["Paris","London","Rome","Berlin","Madrid"]

new_Dict:Dict[str,int]={ key:random.randint(20,30) for key in city_names }

print(new_Dict)


