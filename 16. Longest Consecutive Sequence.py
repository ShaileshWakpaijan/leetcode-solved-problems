# class Solution:
#     def longestConsecutive(self, nums):
#         if len(nums) < 1:
#             return 0
#         sortedNums = sorted(nums)
#         maxCount = 0
#         temp = 0
#         for i in range(1, len(sortedNums)):
#             if sortedNums[i] - sortedNums[i-1] == 1:
#                 temp += 1
#             elif sortedNums[i] == sortedNums[i-1]:
#                 continue
#             else:
#                 maxCount = temp if temp > maxCount else maxCount
#                 temp = 0
#         else:
#             maxCount = temp if temp > maxCount else maxCount
#             temp = 0

#         return maxCount + 1

############## Optimized approach ##############
class Solution:
    def longestConsecutive(self, nums):
        numSet = set(nums)
        maxCount = 0

        for n in numSet:
            if n - 1 not in numSet:
                length = 1
                while n + length in numSet:
                    length += 1
                maxCount = max(length, maxCount)
        return maxCount
                    

            
        

nums = [100,4,200,1,201,202, 203, 204,3,2]
nums2 = [0,3,7,2,5,8,4,6,0,1]
nums3 = [1,0,1,2]

print(Solution().longestConsecutive(nums))
print(Solution().longestConsecutive(nums2))
print(Solution().longestConsecutive(nums3))