# dictionary in memory

# dictionary are indexed by `key` and they can be seen as `associative array`
# python dict are implemented using the `hash tables`
# in case of dictionary the index value get/fetched from the `hash()` i.e hash function on the `key` of the dictionary
# hash table been used for the `key-value lookup`
# in case of the `dictionary` the `key-value pair` can be stored using the `array`
# we can use the `hash()` over the `key` to fetch the `index of the array cell` where the `value` been stored


# A `hash function` maps the `key` to a `hashed value` which is in `numeric form`  and then `index of the array` where the `key-value` pair will going to be get saved
# based on the `key` provided `the hash()` fetch the `index` of the `array cell` where the `value` was stored
# this increases the `performace of the dictionary`


# there are 3 different aspect of the `dictionary`

    # keys
    # hash function
    # array where the values been stored based on the `index value` fetched from the hash function based on the key provided 
    
    
# A good hash function reduces the number of collusion

# collusion:-

    # different `keys` can have the same `hashed values` obtained from the `hash function` which can resolve to `same index` where the `key and values` are stored
    # python does not have the `hash function` which can elemeniate all `collusion`
    # when there is collusion happens then the `the new key-value` pair which has the same index as `before key-value pair` as the hash() return the same index
    # will add the `new key-value` pair as `linked list` to the `old key value pair`
    
