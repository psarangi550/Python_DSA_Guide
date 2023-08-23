# there are many ways thatwe can saearch elements in the dictionary 
# but here we will look into the LinearSearch for search an element in the dictionary 

from typing import Dict,Union

mydict:Dict[str,Union[str,int]]=dict(name="Edy",age=26,address="bangalore")

def searchDict(dict1:dict,value:Union[str,int])->None:
    
    for key in dict1: # for traversing each element then we need the the O(N) time complexity 
        
        if dict1[key]==value: # time complecity id of O(1)
            
            print("Element %s found in dictionary %s" % (value,dict1)) # time complecity id of O(1)
            break # time complecity id of O(1)
            
    else: # time complecity id of O(1)
        
        print("Element %s not found in dictionary %s" % (value,dict1)) # time complecity id of O(1)
        
        
# searchDict(mydict,"Edy")
searchDict(mydict,"edy")


# the time complecity for the searching operation in the dict is of `O(N)` and space complexity of `O(1)`