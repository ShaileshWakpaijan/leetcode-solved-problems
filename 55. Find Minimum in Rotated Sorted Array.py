# Leetcode 153
class Solution:
    def findMin(self, nums):
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + ((r - l) // 2)

            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        print(nums[l])
        return nums[l]