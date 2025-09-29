# Leetcode 239
# class Solution:
#     def maxSlidingWindow(self, nums, k):
#         if k < 1:
#             return []
#         l = 0
#         res = []
        
#         for r in range(k, len(nums) + 1):
#             mx = max(nums[l : r])
#             res.append(mx)
#             l += 1

#         return res

### Solved but not optimized 👆 ###

######## Using Deque ########
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        res = []
        l = r = 0
        q = deque()
        print(q)
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1

        return res


print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(Solution().maxSlidingWindow([1], 1))