# <ins> When to Use or Aviod the Numpy Array </ins> #

- When to Use Array
  
  - When we want to store multiple variables/value of same type 
  - when we want to access random number from array as the time complexity is of O(1)
  - when we want to access the element from the middle from the array in that case the array is very effective 
  - if we are using any other DataType then we have to go for O(N) time complecity as it will start from the beginning
  - but in case of array it will take the O(1) complexity which is very effective

- When Not to Use Array
  
  - Storing the same data type 
  - if we want to define the array of different type of element then we need to use multiple array in that case
  - Reseve Memory (sometime if we just created the array which reserve the memory bit later not used it then those spaces will still be there)
  - when we add element and the array exhust the reserved memory then for adding a=one more element it will add more reserve memory and copy the new element onto the new reservbe memory which is not needed for the element
  - this above can perform the application badly



