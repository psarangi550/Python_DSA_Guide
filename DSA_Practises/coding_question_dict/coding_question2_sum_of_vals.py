from typing import Dict


def merge_dicts(dict1:dict,dict2:dict)->dict:
    
    dict_sum={ key:(value+dict2[key] if key in dict2 else value) for key,value in dict1.items()}
    
    dict2.update(dict_sum)

    return dict2


dict1:Dict[str,int] = {'a': 1, 'b': 2, 'c': 3}
dict2:Dict[str,int] = {'b': 3, 'c': 4, 'd': 5}

# print(merge_dicts(dict1, dict2))

# best approach 

def merge_dicts_best(dict1:dict,dict2:dict)->dict:
    
    for key,value in dict2.items(): # here this is of O(M) complecity
        
        dict1[key]=dict1.get(key,0)+value
        
    return dict1

print(merge_dicts_best(dict1, dict2))

# here the overall time complecity is of O(N) time complecity

# but if we use the copy() to create a separate shallow copy then the time complecity become O(N+M)

# because the copy() takes the O(N) time complecity and we are looping through O(M) time complexity

# the space complexity can be of O(M+N) in the worst case where none of the value in the dict1 and dict2 been matching eacvh can be unique and the merge result can take O(N+M) space 

# the best case can be when the dict1 and dict2 have the same key and same number of element

# in that particular case that will come to O(N/M) complexity as both the size and key being same we can consider one of them 





