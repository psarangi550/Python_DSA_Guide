# treaversing the dict means to access or update each elements in the dictionary
# if we use a for loop over the dictionary then it willl traverse through all the `key of the dictionary `



from typing import Dict,Union


myDict:Dict[str,Union[str,int]] = {"name":"pratik","age":26,"address":"bangalore"}


def traverseDict(dict1:Dict[str,Union[str,int]])->None:
    
    for key in dict1: # the time complecity will be of O(N)
        
        print("Keys---> %s and Values---> %s" % (key,dict1[key])) # the time complecity will be of O(1) and here we are access the key from the dict which is of `O(1) time complexity`

traverseDict(myDict)


# here the time complecity for traversiing the dict is of `O(N)`
# the space complexity for the traversing the element in the dict is of `O(1)` as we don't need an additional space for the same 

