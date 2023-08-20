# find the sum of all the pairs whose sum equal to the given number 

from typing import List

# from itertools import combinations

arr1:List[int]=[2,6,3,9,11]

arr2:List[int]=[3,2,4]

arr3:List[int]=[3,3]

target_number:int=9

target_number:int=6

# for i in range(1,len(arr1)+1):

#     all_combination:combinations=combinations(arr1,i)

#     for item in all_combination:
        
#         if sum(item)==target_number and len(item)>1:
            
#             print(item)

# without using the itertools


def find_pair(arr1,target):
    result:list=[]

    for i in range(len(arr1)):
        
        for j in range(i+1,len(arr1)):
        
            if arr1[i]+arr1[j]==target:
                
                if i not in result and j not in result and arr1[i]!=arr1[j]:
                    
                    result.append(i)
                    
                    result.append(j)
                    
    return result
                
# print(find_pair(arr2,target_number))
# print(find_pair(arr3,target_number))
# print(find_pair([1,2,3,2,3,4,5,6],6))

# best method with O(N) complexity

def find_pair(arr1,target_number):
    
    seen={}
    
    for i , num in enumerate(arr1):
        
        complement=target_number-num # 6-3=3 #6-2=4 #6-4=2
        
        if complement in seen: # 2 present in the list
            
            return [seen[complement],i] #1,2
        
        seen[num]=i # {3:1} {3:0,2:1} 


print(find_pair([3,2,4],6))


# question to ask:--->

# Does this array contains any negetive value 
# What if the pairs repreated twice in the Array , should we need to print it 
# if reverse pair is acceptable or not
# Do we need to print the distinct pair only or does (3,3) count as a valid pair or not (Here in this case it should be distinct)
# How Big is the Array 

        
            
        
    
    
    
    
    
    