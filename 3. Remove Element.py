# class Solution:
#     def removeElement(self, nums, val):
#         for i in range(len(nums)-1, -1, -1):
#             if nums[i] == val:
#                 nums.pop(i)
#         return len(nums)


class Solution:
    def removeElement(self, nums, val):
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
    