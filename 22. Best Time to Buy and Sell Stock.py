# Leetcode 121

class Solution:
    def maxProfit(self, prices):
        maxProf = l = 0

        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                maxProf = max(maxProf, prices[r] - prices[l])

        return maxProf
    
print(Solution().maxProfit([7,1,5,3,6,4]))
print(Solution().maxProfit([7,6,4,3,1]))
print(Solution().maxProfit([1,2,3,4,5]))