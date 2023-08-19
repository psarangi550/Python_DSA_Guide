# A string is a sequence of character where as the list is the sequence of values 
# to convert a string into the list of characters we need to use the list() builtin function passing the string as an args 
# we need to use the list() built in function hence we don't need to use that as the variable in here 
from typing import List

my_str:str='spam'

list1:List[str]=list(my_str)

print(list1)


# if we want to break a sequence of string into words then we can use the split() builtin function
# the split() function will split the sequence of character into multiple words out in here 
# the default implementation of the `split()` function will be for the space character but we can explicitly provide more info 


# we can use the `join()` over the `list` to convert the `list` again back into the `string` format 
my_str2:str="spam-spam-spam"

delimiter:str="a"

list2:List[str]=my_str2.split(delimiter)

# again back to the string we can do that using the join method as 

new_str:str=delimiter.join(list2)

print(new_str)

