class Solution:
    def removeDuplicates(self, nums):
        res = []
        temp = None
        for i in nums:
            if temp != i:
                temp = i
                res.append(i)
        nums.clear()
        nums.extend(res)
        return len(nums)
