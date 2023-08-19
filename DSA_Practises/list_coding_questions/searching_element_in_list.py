# search element in the list can be do by 2 ways 
    
    #1 by using the `in` operator
    #2 by using the LinearSearch algorithm
    
# by using the in operator 

from typing import List,Sequence

list1:List[int]=[x for x in range(10,100,10)]

target:int=50


# by using the in operator in this case we can use it as below
# when using the `in` operator for a list `to search an element` the `time complexity` is of `O(N)` , in worse case where not matching the element
# when  the `element` found then the `search` is successful else the `search` is unsuccessful
# even though we are using the `in` Membership operator python by default perform a `linear Search` to fetch the `particular element`
# the space complexity of the `searching element` is of `O(1)`
# but the `in` Membership operator has better time complecity while `searching in the set/dict which are implemented as the hash tables` compare to the `array/list/tuple` 
# when the `in` Membership operator has better time timecomplexity which is of `O(1)` for the `set/dict` as they implemnented by `hash table`
# but the `set/dict` occupy more space hence the `space complexiity` will not be that efficient , loses the `order and index` of the element


def searchMember(list_ele:list,target:int)->bool:
    
    if target in list_ele:
        
        return True
    
    return False

print(searchMember(list1,target))

# by using the LinearSearch approach by using this
# the time complexity for the linearSearch is of `O(N)` in this case 
# space complecity will be of `O(1)` in this case  
# we can also use the enumerate() to get the both index and value from the list of elements which return the `index and element` as tuple

def searchUsingMember(list_ele:Sequence[int], target:int)->str:
    
    for ele in list_ele: # here the time complecity is of O(N)
        
        if ele == target: # here the time complecity is of O(1)
            
            return "Element %d found in list %s with index as %d" % (ele,list_ele,list_ele.index(ele)) # here the time complecity is of O(1)
    
    return "Element %d Not Found in list %s " % (target,list_ele) # here the time complecity is of O(1)

print(searchUsingMember(list1,target))

# total time complexity of the operation will be of `O(N)` and space complexity is of `O(1)`

    