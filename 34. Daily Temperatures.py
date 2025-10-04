# Leetcode 739

class Solution:
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                _, ind = stack.pop()
                res[ind] = i - ind
            stack.append((temp, i))
        
        return res

print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))
print(Solution().dailyTemperatures([30,40,50,60]))
print(Solution().dailyTemperatures([30,60,90]))
print(Solution().dailyTemperatures([30,38,30,36,35,40,28]))