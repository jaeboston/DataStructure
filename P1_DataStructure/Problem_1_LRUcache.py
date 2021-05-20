# Least Recently Used (LRU) cache. 
# An LRU cache is a type of cache in which we remove 
# the least recently used entry when the cache memory reaches its limit. 
# For the current problem, consider both get and set operations as an use operation.

# Your job is to use an appropriate data structure(s) to implement the cache.

# In case of a cache hit, your get() operation should return the appropriate value.
# In case of a cache miss, your get() should return -1.
# While putting an element in the cache, your put() / set() operation must insert the element. 
# If the cache is full, you must write code that removes the least recently used 
# entry first and then insert the element.
# All operations must take O(1) time.

# For the current problem, you can consider the size of cache = 5.

# Here is some boiler plate code and some example test cases 
# to get you started on this problem:

class Node(object):

  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.next = None
    self.prev = None


class LRU_Cache(object):

    def __init__(self, capacity=10):
        # Initialize class variables
        self.MAX_LEN = capacity

        self.mapCache = {}    #: map to store the key and value
        self.headNode = None
        self.tailNode = None

    def get(self, key):
      """
      retreives the value of the given key

      key: key for the cache
      """
      #: check to see if the key exists
      if key in self.mapCache:
        self.move2Head(key)
        return self.mapCache[key].value #: cache hit
      else:
        return -1 #: cache miss
      

    def set(self, key, value):
      """
      sets the key,value pair into the cache

      key: key for cache
      value: value for cache
      """
      #: check to see if the key exists
      if key not in self.mapCache:
        
        #: Check the current size
        if len(self.mapCache)== self.MAX_LEN:
    
          #: if Cache is full, remove the least recently used 
          self.removeTailNode()

        #: add the new key-value pair to the map
        new_node = Node(key, value)
        self.mapCache[key] = new_node
        self.add2Head(key)


    def removeTailNode(self):
      """
      remove the tail node
      """
      tailNode = self.tailNode
      self.tailNode = self.tailNode.prev
      self.tailNode.next = None

      #: remove from Dictionary
      del self.mapCache[tailNode.key]
      


    def removeNode(self, key):
      """
      remove itself from the linked list
      """
      node = self.mapCache[key]

      if node.prev != None:
        node.prev.next = node.next
      else:
        self.headNode = node.next

      if node.next != None:
        node.next.pre = node.prev
      else:
        self.tailNode = node.prev


    def move2Head(self, key):
      """
      move the most rescently used item to the head
      """
      #: remove the node first
      self.removeNode(key)
      #: move the node to head
      node = self.mapCache[key]

      temp = self.headNode
      self.headNode = node
      node.prev = None
      node.next = temp
      temp.prev = node

    def add2Head(self, key):
      """
      add the most rescently used item to the head
      """
      #: move the node to head
      node = self.mapCache[key]

      temp = self.headNode
      self.headNode = node
      node.prev = None
      if temp != None:
        node.next = temp
        temp.prev = node

#: TEST CASES

#: Init with 5    
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))      #: returns 1
print(our_cache.get(2))      #: returns 2
print(our_cache.get(9))      #: returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

our_cache.set(7, 7)

print(our_cache.get(4))      # returns -1 because the cache reached it's capacity and 4 was the least recently used entry
print(our_cache.get(5))      # returns 5 : 5 is at the tail



#: init with NULL (use default size)
our_cache = LRU_Cache()

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))      #: returns 1
print(our_cache.get(2))      #: returns 2
print(our_cache.get(9))      #: returns -1 because 9 is not present in the cache


#: init with 0
our_cache = LRU_Cache(0)
