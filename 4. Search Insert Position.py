class Solution:
    def searchInsert(self, nums, target):
        count = 0
        while count < len(nums) and nums[count] < target:
            count += 1
        return count

print(Solution().searchInsert([1,3,5,6],1))