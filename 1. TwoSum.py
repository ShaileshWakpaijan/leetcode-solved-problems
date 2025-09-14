# class Solution:
#     def twoSum(self, nums, target):
#         for i in range(len(nums) - 1):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return[]


# Two-pass Hash Table
class Solution:
    def twoSum(self, nums, target):
        numMap = {}
        
        for i in range(len(nums)):
            numMap[nums[i]] = i
        print(numMap)

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]
        else:
            return []
