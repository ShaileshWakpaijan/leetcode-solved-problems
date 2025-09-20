# class Solution:
#     def threeSum(self, nums):
#         numMap = {}
#         res = []
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 numMap[(i, (nums[i])), (j, nums[j])] = nums[i] + nums[j]
            
#         for k in range(len(nums)):
#             for key, value in numMap.items():
#                 if nums[k] + value == 0:
#                     indx = lambda x: x[0]
#                     v = lambda x: x[1]
                    
#                     if indx(key[0]) != indx(key[1]) != k != indx(key[0]):
#                         key = [nums[k], v(key[0]), v(key[1])]
#                         key.sort()
#                         if key not in res:
#                             res.append(key)
#         return res


##################### Using two pointer #####################
class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i, n in enumerate(nums):
            left, right = i + 1, len(nums) - 1
            if i > 0 and n == nums[i - 1]:
                continue
            
            while left < right:
                target =  nums[left] + nums[right] + n
                if target < 0:
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif target > 0:
                    right -= 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1
                else:
                    res.append([n, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res
            
            

print(Solution().threeSum([-1,0,1,2,-1,-4,-1,-1,-1,-1,2,2,2,2,2,2,2]))
# print(Solution().threeSum([0,1,1]))
# print(Solution().threeSum([0,0,0]))
