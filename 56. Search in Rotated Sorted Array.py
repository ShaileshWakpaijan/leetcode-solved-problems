# LeetCode 33

# class Solution:
#     def search(self, nums, target):
#         l, r = 0, len(nums) - 1

#         while l <= r:
#             mid = l + ((r - l) // 2)
#             print(nums[l], nums[mid], nums[r])
#             if nums[mid] == target:
#                 return mid

#             # Left Half
#             if nums[l] <= nums[mid]:
#                 if target > nums[mid] or target < nums[l]:
#                     l = mid + 1
#                 else:
#                     r = mid - 1
            
#             # Right Half
#             else:
#                 if target < nums[mid] or target > nums[r]:
#                     r = mid - 1
#                 else:
#                     l = mid + 1
#         return -1
    

# Using the findMin to split and then do binary search on both sides
class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = l + ((r - l) // 2)
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        
        res = self.binarySearch(0, l - 1, nums, target)
        if res != -1:
            return res
        return self.binarySearch(l, len(nums) - 1, nums, target)
        
    def binarySearch(self, left, right, nums, target):
        l, r = left, right

        while l <= r:
            mid = l + ((r - l) // 2)

            if target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                return mid
        return -1