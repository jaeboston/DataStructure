We include the `calc_hash` function as a method of the `Block` class so that the fuction will have easy access to all the properties of a `Block` class such as the data, the timestamp, and the previous block object. 
The function will update the hash using the `update()` function.
The time complexity would be O(1) constant time.

Then, we implement a class `Blockchain`. It has a root node for a linked list. It uses `append` function to create a `Block` object and link to the previous object. 
The time complexity of the `append` function would be O(N) where N is the number of `Block` objects. 

The space complexity would be O(N) where N is the number of Block objects.
