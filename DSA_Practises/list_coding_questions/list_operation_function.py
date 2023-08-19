# list operations 
    
    # `+` operator :- which being used for the `concartination`
    # `*` operator :- which is being for `multiplication andd creating the multiple list of same type`
    
from typing import List,Sequence

from string import ascii_lowercase

list1:List[int]=[x for x in range(10,100,10)]

list2:Sequence[str]=[x for x in ascii_lowercase[:6]]

print(list1+list2) # type: ignore # here the concartination operation will going to happen in this case 

# using the multiplication operation in here as 

print(2*list2) # type: ignore # using the multiplication operator in this case over here 

# function thjat can be used with list 

    # len(): fetch the total number of element in the list in return
    # max(): we can fetch the maxium array element in the list in return
    # min(): we can fetch the minium array element in the list in return
    # sum(): we can fetch the sum in return
    # we can fetch the average using the `sum(<list>)/len(<list>)`
    
    
# fetching the average using the while loop can be as below 

# count:int=0
# total:int=0

# while (True) :
#     inp:str=input("Entwer a Number")
#     if inp=="done" : break
#     # else block code here 
#     total+=int(inp)
#     count+=1

# print("Average of the input number are %.2f" % (total/count))


# if we want to convert onto the list function we can do that as below 

def convertToList()->str:
    """converting the Above function into List function out in here """
    list1:List[int]=list()
    while True:
        inp:str=input("Entwer a Number")
        if inp=="done" : break
        list1.append(int(inp))
    return "Average of the Input Elements were of %.2f" % (sum(list1)/len(list1))

print(convertToList())    
    
    
     


    
    
    