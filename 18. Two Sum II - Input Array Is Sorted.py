class Solution:
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        res = []

        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                res.append(left + 1)
                res.append(right + 1)
                break
        return res

print(Solution().twoSum([2,7,11,15], 18))