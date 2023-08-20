# using array Datastructure we will implemement this as below

from typing import List

import numpy as np


def average_temperture()->None:
    
    temp_cout:int=int(input("How Many Day's Temperature?: "))
    
    temp_arr:np.array=np.array([])
    
    for i in range(1,temp_cout+1):
        
        input_temp:int=int(input(f" Day {i}'s high temp: "))
        
        temp_arr=np.append(temp_arr,input_temp)
              
    average_temp:float=np.sum(temp_arr) / len(temp_arr)
        
    print(f"Average = {average_temp:.2f}")
    
    def calc_count(item:int)->int:
        
        count:int=0

        if item > average_temp :
            
            count+=1
        
        return count
    
    average_count:List[int]=list(filter(calc_count,[item for item in temp_arr]))   
    
    
    print(f"{len(average_count)}(s) avove the average")
    
    
average_temperture()
            