class Solution:
    def productExceptSelf(self, nums):
        res = {}
        for i in range(len(nums)):
            res[i] = res.get(i, 1)
        
        for j in range(len(nums)):
            for key, value in res.items():
                if key != j:
                    res[key] *= nums[j]

        return list(res.values())
