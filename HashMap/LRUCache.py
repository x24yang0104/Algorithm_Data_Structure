"""
Description
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.
get(key) Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
Finally, you need to return the data from each get.

Example1

Input:
LRUCache(2)
set(2, 1)
set(1, 1)
get(2)
set(4, 1)
get(1)
get(2)
Output: [1,-1,1]
Explanation：
cache cap is 2，set(2,1)，set(1, 1)，get(2) and return 1，set(4,1) and delete (1,1)，because （1,1）is the least use，get(1) and return -1，get(2) and return 1.

Example 2:
Input：
LRUCache(1)
set(2, 1)
get(2)
set(3, 2)
get(2)
get(3)
Output：[1,-1,2]
Explanation：
cache cap is 1，set(2,1)，get(2) and return 1，set(3,2) and delete (2,1)，get(2) and return -1，get(3) and return 2.
"""
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.pre_dict = {}
        self.dummy = Node(0, 0)
        self.tail = self.dummy
        self.curr_size = 0
        
    
    def move_to_tail(self, node):
        self.tail.next = node
        self.pre_dict[node.key] = self.tail
        self.tail = node  
    
    def get(self, key):
        if key in self.pre_dict:
            pre = self.pre_dict[key]
            node = pre.next
            if node is not self.tail:
                pre.next = node.next
                self.pre_dict[node.next.key] = pre
                self.move_to_tail(node)
            return node.val
        return -1
        
    def set(self, key, value):
        if self.get(key) == -1:
            new_node = Node(key, value)
            self.tail.next = new_node
            self.pre_dict[key] = self.tail
            self.tail = new_node
            self.curr_size += 1
            if self.curr_size > self.capacity: 
                head = self.dummy.next
                head = self.dummy.next
                self.pre_dict.pop(head.key)
                self.dummy.next = head.next
                self.pre_dict[head.next.key] = self.dummy 
                self.curr_size -= 1
            
        else:
            self.tail.val = value
  
