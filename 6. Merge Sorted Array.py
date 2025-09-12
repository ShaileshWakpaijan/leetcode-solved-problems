class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        count = 0
        finalLen = m + n
        for i in range(n):
            while nums1[count] < nums2[i] and count < m:
                count+=1
            nums1.insert(count, nums2[i])
            m += 1
        nums = nums1[:finalLen]
        nums1.clear()
        nums1.extend(nums)