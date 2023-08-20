#Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.
# best solution

def find_pair(arr:list,target:int):
    
    final:list=[]
    
    result:list=arr[:]
    
    seen:dict=dict()
    
    for item in arr:
        
        complement=target-item # 7-2=5 # 7-4=3 # 7-3=4 # 7-5=2
        
        if complement in result and result.index(complement)>result.index(item):
            
            seen[item]=complement # {2:5} # {2:5,4:3} # {}
            
            result.remove(item)
        
    for key,value in seen.items():
        
        final.append(f"{key}+{value}")
    
    return final
        


# print(find_pair([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))


# another approach but with O(N2) complecity

def fetch_pair(arr:list,target:int)->list:
    
    result:list=[]
    
    for i,ele in enumerate(arr):
        
        for j in range(i+1,len(arr)):
            
            if arr[i]+arr[j]==target :
                
                result.append(f"{arr[i]}+{arr[j]}")
                
    return result


print(fetch_pair([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))


                

