# Leetcode 239
class Solution:
    def maxSlidingWindow(self, nums, k):
        if k < 1:
            return []
        l = 0
        res = []
        
        for r in range(k, len(nums) + 1):
            mx = max(nums[l : r])
            res.append(mx)
            l += 1

        return res

# Solved but not optimized 👆

print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(Solution().maxSlidingWindow([1], 1))