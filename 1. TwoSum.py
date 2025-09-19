# class Solution:
#     def twoSum(self, nums, target):
#         for i in range(len(nums) - 1):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return[]


# Two-pass Hash Table
# class Solution:
#     def twoSum(self, nums, target):
#         numMap = {}
        
#         for i in range(len(nums)):
#             numMap[nums[i]] = i
#         print(numMap)

#         for i in range(len(nums)):
#             complement = target - nums[i]
#             if complement in numMap and numMap[complement] != i:
#                 return [i, numMap[complement]]
#         else:
#             return []
        
# One-pass Hash Table
class Solution:
    def twoSum(self, nums, target):
        numMap = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]
            numMap[nums[i]] = i
        else:
            return []

print(Solution().twoSum([2,7,11,15], 9))
print(Solution().twoSum([2,7,11,15], 26))
print(Solution().twoSum([3,2,4], 6))
print(Solution().twoSum([3,3], 6))