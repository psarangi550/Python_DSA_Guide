# <ins>  Time and space complexity Of Dictionary </ins> #

|  Operation               | Time complexity      | Space complexity |
|--------------------------|:--------------------:|-----------------:|
| creating an empty dict |        O(1)          |  O(1)     |                  
| creating an dict with N elements| O(N)      |   O(N)    |
|inserting a row/column in an array | O(1)/O(N) | amortized O(1) |
| Traversing a given dict | O(N) | O(1) |
| Accessing a value from dictionary  | O(1)  | O(1) |
| Searching for a given value in dictionary using LinearSearch | O(N) | O(1) |
| deleting an Element from Array | O(1) | O(1) |


- when we create a `Dictionary` for each of the key `hash function` will be applioed and then create the `hash table` and then create the `corresponding index for the same` hence the `time complexity` will be of `O(N)` time complxity

- inserting the `key-value pair` will be of `O(1)` time complexity , Based on the `hash function` vcalculation from the `key` provoided it can go to `O(N)` which is of very rare and hence the time complexity will be of `O(1)` time complexity mostly

- `hash function` took little time to calcuate the `index` where the `Key-value pair` stored in the array based on the `key` provided to the same , hence accessing the element is of `O(1)` time complexity

- but if we are `searching using the in operator` bassed on particular key/value we can fetch the `index of the key-value pair` based on the key provided which is much faster 

- as in case of the `delete` we are accessing the `index of key-value pair` based on the `hash function with the key provided` which is faster to access and delete the same hence the time complecity will be of `O(N)`

