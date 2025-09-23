# LeetCode 3
# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         l = 0
#         maxCount = 0
#         trackSet = set()

#         for c in s:
#             if c not in trackSet:
#                 trackSet.add(c)
#                 maxCount = max(len(trackSet), maxCount)
#             else:
#                 while s[l] != c:
#                     trackSet.remove(s[l])
#                     l += 1
#                 l += 1

#         return maxCount

######## Using Sliding Window ########
class Solution:
    def lengthOfLongestSubstring(self, s):
        l = 0
        maxCount = 0
        trackSet = set()

        for r in range(len(s)):
            while s[r] in trackSet:
                trackSet.remove(s[l])
                l += 1
            trackSet.add(s[r])
            maxCount = max(maxCount, r - l + 1)
        return maxCount
    
print(Solution().lengthOfLongestSubstring("bcadabcbb"))
print(Solution().lengthOfLongestSubstring("pwwkew"))
print(Solution().lengthOfLongestSubstring(""))