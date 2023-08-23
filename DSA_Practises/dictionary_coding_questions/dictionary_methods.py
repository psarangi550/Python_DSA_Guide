# All dict() methods available for dictionary

    # clear() :- this method remove all the entry of the dictionary 
        # it does not take any args or does not return any value in return
        
    # copy() :- this return the `shallow copy` of the dictionary that provided as the args 
        
        # it does not modify the original dictionary
        # rather create a new dictionary with the copy reference to the original dictionary
        # copy() also does not take any args 
        # copy() return the shallow copy of the original dictionary in return 
        
    # fromkeys():-

        # the fromkeys() method create a dictionary with a given sequence of element with value provided  
        # this only be called on a dictionary object 
        # the syntax of fromkeys method is of `<dict obj>.fromkeys(sequence[],value)`
        # the fromkeys() takes the first args as the Sequence which can be used as the key of the dictionary 
        # the  fromkeys() method takes the 2nd args the values which isa the optional args 
        # values will be set as the values provided into the dictionary 
        # if we are not providing the value then the values come down to None in this case
       
       
from typing import Dict,Union 

import string
        
# we can use the fromkeys() as below 

my_new_dict:Dict[str,int]=dict().fromkeys([alpha for i, alpha in enumerate(string.ascii_lowercase) if i<4],10)

print(my_new_dict)

    # get()

        # the get() return the values from the specified key if key found else return None 
        # we can also pass the optional value to the get() function when the key not found then it will return the default value provided to it 
        # the value  in the get() is optional in nature 

    # items()

        # items() return a `view object` which is in the form of `list of dictionary key, value pair as tuple`
        # the items() can be called on a dictionary object 
        # this will not take anything as args and return the  key-value as tuple inside the list instead as view object whyich is of `dict_items` types
        # this is similar to the view items method in python 2.7
        
myDict:Dict[str,Union[str,int]]={"name":"pratik","age":30,"address":"Bangalore","education":"btech"}

print(myDict.items())

    # keys()

        # the keys() methoid return a view object which is in the form of the `dict_keys` with list of keys present in the dictionary 
        # like the items() method the keys() can be called on a dictionary object and does not take any args 
        # this will return a view object with the name as `dict_keys` with the list of key present  in the dictionary
        # when the dictionary changes the corresponding view object which contains the list of keys will going to get changed 
        
        
    # popitem()

        # the popitem() will remove and return the last value which been inserted to the dictionary 
        # the popitem() before python 3.7 will remove the random element from the dictionary
        # but now after 3.7 popitem() will return the last value which being inserte after deleting the same 
        # the popitem() does not take any args but return the alue which being deleted and key value as tuple pair 
        # we can apply the popitem() method the dictionary object for reference 
        
        
    # pop()

        # the pop() will remove and return the value of the key which been passed as args to the pop()
        # its take the key as the args and  can be called upon the dictionary object 
        # if the key not present in the dict then it will throw a keyerror
        # in order to avoid the same we can provide the 2nd value which can be passed to the pop() so in case of the key not found treturn that instead of giving keyError
        
        
        
    #setdefault()

        # the setdefault() return the value from the dictionary if the corresponding key being present , if key not present then return the insert the `key` with the value provided into it 
        # the setdefault() method will take 2 parameter which is off 

            # key of the dictionary to be searched in the dictionary 
            # value to be associated if the key not found in the dictionary and return that specific value 
            # if value provided to the setdefault() method is option if not provided then takes None as the default value
            
myDict:Dict[str,Union[str,int]]={"name":"pratik","age":26,"address":"banagaloe"}

return_value1:Union[str,int]=myDict.setdefault("education","btech")

return_value2:Union[str,int]=myDict.setdefault("age",27)      

print(return_value1)

print(return_value2)
        
    # values()

        # the values() methoid return a view object which is  inthe form of `dict_values` with list of values present in the dictionary 
        # the values will contains the list of values that can be provide to the values() method
        # values() can't take any arguments inside it but return a view object of `dict_values` with the List of values from the dictionary 
        
        
    # update()

        # update() will update the existing dictionary from the element of another dictionary or from an iterable of key-value pair as tuples
        # if the key is not in the dictionary it will add the key-value pair to the existing dictionary
        # if the key is already present then update the value associated with it 
        # it can be applied on the dictionary object 
        # as an args wee can pass another dict or Sequence of key-value pair as the tuples 
        # this method will return nothing but existing dict will be going to be get updated
        
        
            
myDict:Dict[str,Union[str,int]]={"name":"pratik","age":26,"address":"banagaloe"}

myDict1:Dict[str,Union[str,int]]={"role":"developer","address":"London"}

# we can also pass the Sequence as the tuple in here as below 

myDict.update(myDict1)

print(myDict)

myDict.update([("company","siemens"),("project","li"),("address","Bhubaneswar")])

print(myDict)
        
        
        
        
        
        
         
        
        
        
        