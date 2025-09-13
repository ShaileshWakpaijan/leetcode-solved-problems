# class Solution:
#     def containsDuplicate(self, nums):
#         for i in range(len(nums)):
#             if nums[i] in nums[i + 1:]:
#                 return True
#         else:
#             return False

# Final Submission
   
class Solution:
    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            print(i)
            if nums[i] == nums[i - 1]:
                return True
        return False

