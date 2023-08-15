from typing import Union

import string 

# convert array to string using thr tostring() method

# splice Elements from an Array 
# Append a string to char array using the fromstring() method

#1 create an array and traverse and access individual element using the indexes 

from array import * 

# the interger Size in the python is of `2 Bytes`

arr1=array("i",[1,2,3,4,5,6])

# fetching each element using the membership operator 

for index in arr1:
    print(index)

# the time complecity for this will be of O(N)


# fetching the individual Element in here 
print(arr1[0])
    
# the time complecity for this will be of O(1)

#2 Append any value to the array using the append() method

arr1.append(7)

print(arr1)

# here the time complexity is of O(1)

#3 extend python array using the extend() method

arr1.extend([8,9,10])

my_additional_values=array("i",[11,12,13])

arr1.extend(my_additional_values)

print(arr1)

# here also the time complexity is of O(N)

# but the space complexity will be of  O(N)

#4 insert a value into the array using the insert() method

arr1.insert(0,0)

print(arr1)

# here the time complecity will be 0(N) and space complexity as O(1)

#4 Add Items From List into the array using the fromlist() method

# it does the same work as the extend() but works on the front of List

list1:list = [14,15,16]

# here we are adding the values from the List 

arr1.fromlist(list1)

print(arr1)


#5 remove any element using the remove() and  remove last element using the pop() method 

arr1.remove(14) # removing the elemnt from the List based on the element that we have provided 

# in case of the multiple occurances then remove() will remove the `first occurances` of the element 

print(arr1)

# here the time complecity of the operation if of O(N) and space complexity is of O(1)

# removing the element from the end of the array using the pop() 

# here the time complecity and space complexity over here id of O(1) and O(1)

arr1.pop()

print(arr1)

#6 fetch element based on the index using the index()

print(arr1.index(15))

# if the element not found then the index method will return IndexError

# print(arr1.index(18))

def fetchIndex(arr1:array, index: int)->Union[int,str]:
    
    for ele in arr1:
        
        if ele==index:
            
            return arr1.index(ele)
    
    return "Element Not Found"


print(fetchIndex(arr1,18))
            

#7 reverse an array using the reverse() method

arr1.reverse()

# reverse() will return nothing on applied but the existing Larray element going to be get reversed 

print(arr1)

# we can also use the reversed() on the array as 

reversed_arr1=reversed(arr1)

# here we are type casting it to the array element as below 

arr2=array("i",reversed_arr1)

print(arr2)

#8 check the array buffer info using the buffer_info() method

# this will provide the provide the `array buffer start adderess in the memory` info and the `number of element in the array `

arr3_5=array("i",[x for x in range(10)])

print(arr3_5.buffer_info()) # this will provide the memory location of the array first element and number of element present in the array

# this will show what is the array buffer info in here 

print(id(arr3_5))

#9 check the number of occurances using the count() method 

# when we use the count() then it fetch the `Number of occurances` of that element

element=11

arr2.insert(0,12)

print(arr2.count(12))

print(arr2.count(18))

# the count() will return the `0` when the element not found on the array 

#10 convert array to python list with the same element using the tolist() method 

arr3=array("i",[x for x in range(1,10)])

list2=arr3.tolist()

print(type(list2))

print(list2)


#11 convert array to string using thr tostring() method

# from python 3.9 and later that method changed to tobytest() and frombytes() methods in python

# representing the string array there are 2 ways in here 

# by using the byte striing using thwe ord value

arr4=array('b',map(ord,["a","b","c"]))

print(arr4)

# if we want to conver the byte str into the string then we can do it s below 

str_ele=map(chr,arr4)

# then we can use the join() as below 

print(" ".join(str_ele))


# using the unicode value as u in here 

arr5=array('u',[x for x in string.ascii_lowercase])

print(arr5)

byte_str1=arr5.tobytes()

print(type(byte_str1))

print(byte_str1)

# if we want to convert the array into the string we can use the join() in that case as below 

print("".join(arr5))


#12 splice Elements from an Array 

# here we can slice the Array based on the index value as below 

arr9=array("i",[x for x in range(6)])

print(arr9[2:4])

#13 Append a string to char array using the fromstring() method

# the fromstring method convert the `byte string` to the specific type of object once it converted by using the tobytes() method

arr6=array('i',[x for x in range(10)])

# converting to the byte using the tobytes() method

print(arr6)

byte_arr6=arr6.tobytes()

print(byte_arr6)

# converting back to the original int array using the fromstring()

arr7=array("i")

# creating an empty integer array in here 

# we can take the input as byte_string from the array which is conveted using the `tobytes()` method and create an empty array and inserted back to the empty array using the method as frombytest()

arr7.frombytes(byte_arr6)

# here applying the frombytes() on the array object

print(arr7)

# we can create the char array and append the string to the char array using the frombytest() method as below 

arr8=array("u",[x for x in string.ascii_lowercase])

print(arr8)

byte_str=arr8.tobytes()

arr9=array("u")

array.frombytes(arr9,byte_str)

# when we are applying on the array module we can pass 2 params in this case 
# when we are applying onn the single array object we need to pass ony one element into the same 

print(arr9)