class Solution:
    def topKFrequent(self, nums, k):
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1

        sortedList = sorted(d.items(), key=lambda x: x[1], reverse=True)
        return [key for key, value in sortedList[:k]]
        

print(Solution().topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))