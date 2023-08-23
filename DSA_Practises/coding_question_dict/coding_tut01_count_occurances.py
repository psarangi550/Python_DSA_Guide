from typing import List,Dict

def countWords(arr1:List[str])->Dict[str,int]:
    
    counter:Dict[str,int]=dict()
    
    for ele in arr1:
        
        counter[ele]=counter.get(ele,0)+1
        
    return counter

words:List[str] = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 

print(countWords(words))