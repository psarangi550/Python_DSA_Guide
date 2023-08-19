# <ins> Time and Space Complexity for List Operation </ins> #

|  Operation               | Time complexity      | Space complexity |
|--------------------------|:--------------------:|-----------------:|
| creating an empty list  |        O(1)          |  O(1)     |                  
| creating a List with elements|O(N)      |   O(N)    |
|inserting an Element into the List | O(N) | O(1) |
| Traversing a given List | O(N) | O(1) |
| Accessing an Element from List | O(1)  | O(1) |
| Searching for values in List | O(N) | O(1) |
| Deleting an Element from List | O(N) | O(1) |


- when we create an `emptyList` then the `interpreter` intilizes the `List with No element` but the `list object` Hence its a constant time operation 
- only the `empty list object` with `metadata` will be initiated for same with the info such as `length of the List and capcity of the List ` and hence time complecity is of `O(1)`
- hence as we are adding the `empty list` then we don't have to add the `additional memory` into the same , hence space complecity is of `O(1)`

- the memory will be used for `pointer` to the `list element` and `other metadata`
- when we create element with `List Element` then it should have the `memory being used for the pointer to the List Element and List Object` and `intialize the element with the value`
- hence the time complexity of creating the element of `n element` is of `O(n)` and `O(n)`

- when we `insert a new element to the list additional space not required to allocated the new value` and hence the time complecity is of `O(1)`

- when we are deleting the `element from the List` then we need to provide the `time complecity of O(N)` as we are deleting `first element` then `all the element after that need to be moved`

