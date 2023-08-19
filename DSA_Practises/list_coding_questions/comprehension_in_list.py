# list comprehension in python 

# we are creating a New List from the Existing List , we can do that using the for loop as well (which can be time consuming)
# the format for creating the new List from the existing one is by using it as `[<new item> for <item> in <list>]`]

# we can use the List comprehension for
    
    # List
    # Range
    # String
    # Tuple ----> Generator will be created for this 

from typing import List

list1:List[int]=[1,2,3,4,5]

list2:List[int]=[x*2 for x in list1]

print(list2)


# conditional List Element in here
# the structure of the List comprehension with conition will be of `[<new item> for <item> in <list> if <condition>]` or `[<new item> if <condition> else <value> for <item> in <list>]`
# this will help in creating the new element if the condition is matched or met

prev_list1:List[int]=[-1,10,-20,2,-90,60,45,20]

# if we want to create a List with positive number then we can do that as 

new_list:List[int]=[item for item in prev_list1 if item > 0]

print(new_list)

# square of the negetive number can be of 

new_negetive_square_list:List[int]=[item**2 for item in prev_list1 if item < 0]

print(new_negetive_square_list)


# fetch the consonant over here 

sentence:str="My Name is Pratik"

# now fetching the value as below which will fetch the consonant only

list_of_consonants:List[str]=[sent for sent in sentence if sent not in ["a","e","i","o","u"]+list(map(str.upper,["a","e","i","o","u"])) and sent.isalpha()]

print(list_of_consonants)

# when number less than 0 then consider that as 0 else the number itself

list_mod:List[int]=[item if item > 0 else 0 for item in prev_list1 ]

print(list_mod)

# another approach 

def getNumber(number:int)->int:
    
    return number if number > 0 else 0

list_mod1:List[int]=[getNumber(item) for item in prev_list1]

print(list_mod1) 