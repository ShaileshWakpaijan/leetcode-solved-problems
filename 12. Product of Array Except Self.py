# class Solution:
#     def productExceptSelf(self, nums):
#         res = {}
#         for i in range(len(nums)):
#             res[i] = res.get(i, 1)
        
#         for j in range(len(nums)):
#             for key, value in res.items():
#                 if key != j:
#                     res[key] *= nums[j]

#         return list(res.values())

# With O(n) time and space complexity
# class Solution:
#     def productExceptSelf(self, nums):
#         prefix  = []
#         suffix  = []
#         prefix.append(1)
#         suffix.append(1)
#         for i in range(1, len(nums)):
#             prefix.append(nums[i - 1] * prefix[i - 1])

#         for j in range(len(nums) - 2, -1, -1):
#             suffix.append(nums[j + 1] * suffix[-1])

#         for k in range(len(nums)):
#             nums[k] = prefix[k] * suffix[-(k + 1)]
        
#         return nums

# With O(n) time and O(1) space complexity
class Solution:
    def productExceptSelf(self, nums):
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1 , -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res