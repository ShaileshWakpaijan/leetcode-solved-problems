# brute force approach
class Solution:
    def maxArea(self, height):
        maxAr = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                maxAr = max(min(height[i], height[j]) * (j - i), maxAr)
        
        return maxAr

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
print(Solution().maxArea([1,7,2,5,4,7,3,6]))
print(Solution().maxArea([1,1]))
print(Solution().maxArea([2,2,2]))