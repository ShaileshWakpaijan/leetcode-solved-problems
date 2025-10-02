# Leetcode 3100
class Solution:
    def maxBottlesDrunk(self, numBottles, numExchange):
        empBtl = numBottles
        maxDrink = numBottles
        crrExchange = numExchange

        while empBtl >= crrExchange:
            empBtl = (empBtl - crrExchange) + 1
            maxDrink += 1
            crrExchange += 1
        return maxDrink


print(Solution().maxBottlesDrunk(13, 6))
print(Solution().maxBottlesDrunk(10, 3))
print(Solution().maxBottlesDrunk(5, 0))