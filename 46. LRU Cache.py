# Leetcode 146

# Worst solution using list and hashmap
# class LRUCache:
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.hashMap = {}
#         self.cacheList = []

#     def get(self, key: int) -> int:
#         if key in self.hashMap:
#             self.cacheList.remove(key)
#             self.cacheList.append(key)
#             return self.hashMap.get(key)
#         return -1

#     def put(self, key: int, value: int) -> None:
#         keys = self.hashMap.keys()
#         if len(keys) > self.capacity and key not in self.hashMap:
#                 oldest_key = self.cacheList.pop(0)
#                 del self.hashMap[oldest_key]

#         if key in self.hashMap:
#             self.cacheList.remove(key)
#         self.hashMap[key] = value
#         self.cacheList.append(key)


# Optimal solution using Doubly Linked List and Hashmap
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
    
    def remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
    
    def insert(self, node):
        node.prev, node.next = self.right.prev, self.right
        node.prev.next = self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if len(self.cache) >= self.capacity and key not in self.cache:
                del self.cache[self.left.next.key]
                self.remove(self.left.next)

        if key in self.cache:
            self.remove(self.cache[key])
        newNode = Node(key, value)
        self.insert(newNode)
        self.cache[key] = newNode