class Solution:
    def threeSum(self, nums):
        numMap = {}
        res = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                numMap[(i, (nums[i])), (j, nums[j])] = nums[i] + nums[j]
            
        for k in range(len(nums)):
            for key, value in numMap.items():
                if nums[k] + value == 0:
                    indx = lambda x: x[0]
                    v = lambda x: x[1]
                    
                    if indx(key[0]) != indx(key[1]) != k != indx(key[0]):
                        key = [v(key[0]), v(key[1]), nums[k]]
                        key.sort()
                        if key not in res:
                            res.append(key)
        return res

print(Solution().threeSum([-1,0,1,2,-1,-4]))
print(Solution().threeSum([0,1,1]))
print(Solution().threeSum([0,0,0]))