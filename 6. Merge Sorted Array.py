# class Solution:
#     def merge(self, nums1, m, nums2, n) -> None:
#         count = 0
#         finalLen = m + n
#         for i in range(n):
#             while nums1[count] < nums2[i] and count < m:
#                 count+=1
#             nums1.insert(count, nums2[i])
#             m += 1
#         nums = nums1[:finalLen]
#         nums1.clear()
#         nums1.extend(nums)

# Another approach
class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1
        while j >= 0:
            if i >= 0 and nums2[j] < nums1[i]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
