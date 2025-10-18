# Leetcode 146

# Worst solution using list and hashmap
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashMap = {}
        self.cacheList = []

    def get(self, key: int) -> int:
        if key in self.hashMap:
            self.cacheList.remove(key)
            self.cacheList.append(key)
            return self.hashMap.get(key)
        return -1

    def put(self, key: int, value: int) -> None:
        keys = self.hashMap.keys()
        if len(keys) > self.capacity and key not in self.hashMap:
                oldest_key = self.cacheList.pop(0)
                del self.hashMap[oldest_key]

        if key in self.hashMap:
            self.cacheList.remove(key)
        self.hashMap[key] = value
        self.cacheList.append(key)

