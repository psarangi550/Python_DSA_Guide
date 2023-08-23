def check_same_frequency(list1, list2):
    
    dict1={ele:list1.count(ele) for ele in list1}
    
    dict2={ele:list2.count(ele) for ele in list2}
    
    if dict1==dict2:
        
        return True
    
    return False
    
list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]

print(check_same_frequency(list1, list2))


# best approach 

def check_same_frequency_best(list1, list2):
    
    def count_list_gen(list3):
        
        counter={}
        
        for ele in list3:
            
            if ele not in counter:
                
                counter[ele]=1
                
            else:
                
                counter[ele]+=1
                
        return counter
    
    return count_list_gen(list1)==count_list_gen(list2)

print(check_same_frequency_best(list1, list2))


# in case of the best case scenario the time complexity will be off O(N+M) where N and M are the lenght of the List and also minimum distinct element of the List which will be created as the dictionary else it will be added to the value 
# hence the overall time complecity for the function is of O(N+M+Min(N,M))
# the space complecity of O(N+M) where N and M are the dictinct element of the List which will create the New dict which will consume the space 