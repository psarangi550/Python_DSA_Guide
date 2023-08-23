def max_value_key(my_dict):
    
    max_value=[0,""]
    
    for key,value in my_dict.items():
        
        if value>max_value[0]:
            
            max_value=value,key
            
    return max_value[1]


my_dict = {'a': 5, 'b': 9, 'c': 2}


# print(max_value_key(my_dict))
# best approach using the max() with the key  params which will decide using which we can fetch the value

def max_value_key_best(my_dict):
    
    return max(my_dict,key=my_dict.get)

print(max_value_key_best(my_dict))

# here the time complecity will be of O(N) and space complecity is of O(1)