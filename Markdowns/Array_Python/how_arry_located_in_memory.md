# <ins> How Arrays are located in the Memory </ins> #

- when we use the `one dimentional array` in the `RAM`  the compiler stored as ` <block defined in the array> contiguous cell in the Memory`

- all the `elements` are the stored in the `contiguous memory` that is `they will be located next to each other `

- there will be no gap between the `contiguous memory location` which being `gurantee by the system ` which is the nature of array 

- in case of the `Two Dimentional Array` in the memory they will be represented as the `One dimentional Array only`

- two dimentional array they will be represented by one dimentional array as 

    - system combine the two dimentional array make it as a single one dimentional array over here 

- in  case of the `Three Dimentional Array` can be represented by 

    ```
    # The Three Dimentional Array can be represented as below 
        [[
            [
                [0,1,2], # here it represent the depth as 0 and Row value as 0 and column value as 0,1,2
                [3,4,5]  # here it represent the depth as 0 and Row value as 1 and column value as 0,1,2
            ],
            [
                [6,7,8],   #here it represent the depth as 1 and Row value as 0 and column value as 0,1,2
                [9,10,11]  #here it represent the depth as 1 and Row value as 1 and column value as 0,1,2
            ],
            [
                [12,13,14], #here it represent the depth as 2 and Row value as 0 and column value as 0,1,2
                [15,16,17], #here it represent the depth as 2 and Row value as 1 and column value as 0,1,2
            ]
        ]]

    ```

    - here also in this case all the `elements in the three dimentional array` will be located as `single dimentional array` in the `RAM` saved by the `compiler`

    - they will be sved in the format as below 

        ```
            
             depth as 0 and Row value as 0 and column value as 0,1,2,depth as 0 and Row value as 1 and column value as 0,1,2,here it represent the depth as 1 and Row value as 0 and column value as 0,1,2,depth as 1 and Row value as 1 and column value as 0,1,2,depth as 2 and Row value as 0 and column value as 0,1,2,depth as 2 and Row value as 1 and column value as 0,1,2

            # which can be represented as below 
            0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,16,17 # this will be single dimentional memory representation of the 3 diemtional Array 
        
        ```
