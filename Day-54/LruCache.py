''' Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4'''

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.memory={}
        self.stack=[]
        self.capacity=capacity


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # if key is present in the memory
        if key in self.memory:
            # update LRU stack
            self.updateStack(key)
            # return the value
            return self.memory[key]
        # else return -1
        return -1

    def updateStack(self,key):
        # if key is already present in the stack
        if key in self.stack:
            # get it's current index and remove it
            curIndex=self.stack.index(key)
            self.stack.pop(curIndex)
        # add the key in to the LRU stack    
        self.stack.append(key)    
            
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # if the memory is full and the key is not present
        if len(self.memory)==self.capacity and (key not in self.memory):
            # remove the least used item from stack and memory
            lastKey=self.stack.pop(0)
            self.memory.pop(lastKey)
        # add/update the key in stack and memory     
        self.memory[key]=value
        self.updateStack(key)