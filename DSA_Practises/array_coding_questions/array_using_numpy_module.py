import numpy as np #importing the numpy module in here 

# we can create the numpy array using the below syntax as 
np_array=np.array([],dtype=int)
#using the array() on the numpy module we can create the numpy array in python
# here we can put the `dataype` as the `dtype` as keyword args in here 
print(np_array) # this will provide the empty array as `[]` which will be going to be get created 
print(type(np_array)) # this will belong to the <class 'numpy.ndarray'> class 

# when we are creating an empty array using the `numpy module` then `no memory been allocated` for the `array` inside the `RAM` as there is no more element
# only the `empty numpy array object` will be stored to the `RAM memory` with the reference as `np_array` which contain the metadata info such as `type of object store to the Array`

# if we want to create the `numpy array` with the element which can occupy `contiguous space` in the memory then we can use as below term 
# in the below case a `contiguous memory block` on the `RAM` being used to store the info out in here 
np_array1=np.array([1,2,3,4],dtype=int) # creating the numpy array with 4 interger element using the numpy module 
print(np_array1)

# the size of the `contiguous memory block` depends on the 

    # number of the element 
    # shape of the array 
    # DataType we are using for the Array
    
# the advance of numpy that it provide an array which is off 
    # feature-rich  
    # hight performing 
    # which support wide range of numeric operation and functions
    
    
#