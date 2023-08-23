# <ins> Dictionary in Python </ins> #

- A `dictionary` `is a collections` which is `unordered, changable and indexed `
- Like we have `dictionary` for the `word` and `meaning as its value` similarly the `dictionary` has `key and value pair`
- as the `data` kept in `key-value` pair hence we can retrieved the `value` using `key`
- we can fetch the `value` using the syntax as `<dict name>[<key>]`
- in case of the `sequence` does not matter as we can fetch the element `value` by their corresponding `key`

- in List or array the should be of `integer` type but in case of `dictionary` the `key` can be `int/float/str..etc`

# <ins> Dictionary in Details </ins> #

- A `dictionary` is a mutable `collections of key and vlue pair` where `each unique key` map to the corresponding `value`
- `dictionary` were implemented using `hash tables` which provide `fast access to the values` base on the `key provided`
- we can create an `empty dictionary` using the `dict constructor` which is `dict()` or using the `{}`
- the time complexity of the `creating an empty dictionary` is of O(1) and the `space complecity` is of `O(1)` as the `intitial hash table structure een allocated`
- we can create a `dictionary with element ` as `dict(key1=value1,key2=value2,key3=value3)`
- but while defining as above we don't have to pass the `key` with the `string format`rather we can provide that as `string format`
- for creating the `dictionary` of `n key value pair` will be of `O(N)` and space complecity is of `O(N)`
- as each `key-value` pair need to be inserted into the `dictionary` hence the `time and space complexity` will be of `O(N)`
- we can also use the `dict()` constructor with the `list of tuple` 
- 