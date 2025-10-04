# Leetcode 853

class Solution:
    def carFleet(self, target, position, speed):
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        stack = []

        for p, s in cars:
            t = (target - p) / s
            stack.append(t)
            if len(stack) > 1 and t <= stack[-2]:
                stack.pop()
        
        return len(stack)

print(Solution().carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))
print(Solution().carFleet(100, [0,2,4], [4,2,1]))
print(Solution().carFleet(10, [3], [3]))