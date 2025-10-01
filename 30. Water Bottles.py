# Leetcode 1518
class Solution:
    def numWaterBottles(self, numBottles, numExchange):
        remaining = numBottles
        maxDrink = numBottles

        while remaining >= numExchange:
            crrDrink = remaining // numExchange
            maxDrink += crrDrink
            remaining = crrDrink + (remaining % numExchange)
        return maxDrink

print(Solution().numWaterBottles(9, 3))
print(Solution().numWaterBottles(15, 4))
print(Solution().numWaterBottles(16, 4))