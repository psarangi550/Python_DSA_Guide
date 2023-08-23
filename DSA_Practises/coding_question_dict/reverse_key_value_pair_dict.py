def reverse_dict(my_dict):
    
    return {value:key for key,value in my_dict.items()}

# here the time complecity is of O(N) as we are looping through all the items 

# the space complecity will be of O(N) as we are traversing and creating a New dict element using the dict comprehension 

def filter_dict(my_dict, condition=None):
    
    return { k:v for k,v in my_dict.items() if condition(k,v) }

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4} 

filtered_dict = filter_dict(my_dict, lambda k, v: v % 2 == 0) 

print(filtered_dict)

# print(filter_dict(my_dict))