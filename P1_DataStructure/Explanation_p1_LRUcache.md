To satisfy the requirement of O(1) time complexcity for all operation, I used Dictionary to store key,value pair data.
Also, I used doubled LinkedList to store keys. The most recently used key would be placed at the head of LinkedList.
This process puts the least recently used key at the tail of LinkedList automatically, creating a Queue like behaviror using LinkedList.

For example, when we add a new key,value pair, we check the Dictionary object has reached to the full capacity or not.
If it is at its full capacity, we can simply delete the tail key, add the pair to the Dictionary object ,and add the key to the head of the LinkedList object.

All of the above steps takes O(1). Dictionary can add a key,value pair in O(1) operation.
LinkedList can add and remove a node in O(1) operation as well.

The space complexity would be O(N) where N is the the capacity.