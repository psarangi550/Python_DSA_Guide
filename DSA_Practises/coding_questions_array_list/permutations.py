# permutation with string 
# given two string find whether one is a permutation of another string or not 
# if two string are permutation of each other if they have the same letter but in differwent order of it 
# ex:-

    # peek - keep
    # rail -liar
    
from typing import List
    
def fetchPermutation(str1:str,str2:str)->bool:
    
    list1:List[str]=list(str1)
    
    list2:List[str]=list(str2)
    
    for item in list1:
        
        if item in list2 and len(list1)==len(list2):
            
            continue
        
        else:
            
            return False
    
    return True
            

print(fetchPermutation("liar","rail"))  

     
# we can do that using sorting as well 

def fetchPermutationBest(str1:str,str2:str)->bool:
    
    list1:List[str]=list(str1)
    
    list2:List[str]=list(str2)
    
    if len(list1)==len(list2):
        
        list1.sort()
    
        list2.sort()
        
        for i ,ele in enumerate(list1):
            
            if ele==list2[i]:
                
                continue
            
            else:
                
                break
                
        else:
        
            return True
    
    return False

            
print(fetchPermutationBest("liar","ail"))  


def fetchPermutationAnotherBest(str1:str,str2:str)->bool:
    
    list1:List[str]=list(str1)
    
    list2:List[str]=list(str2)
    
    if len(list1)==len(list2):
        
        list1.sort()
    
        list2.sort()
        
        if list1==list2: # when we compare the List each element of the list compared with each element in the other list if in case all the values are same then True will be returned
            
            return True
    
    return False

print(fetchPermutationBest("liar","rail"))  