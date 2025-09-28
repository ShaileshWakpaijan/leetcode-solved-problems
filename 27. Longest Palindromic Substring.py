# Leetcode 5
import math

# I have used Neetcode solution to solve this
class Solution:
    def longestPalindrome(self, s):
        res = ""
        resLen = 0
        strLen = len(s)

        for i in range(len(s)):
            if i >= (strLen - math.ceil(resLen//2)):
                break

            l, r = i, i
            while l >= 0 and r < strLen and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = len(res)
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while l >= 0 and r < strLen and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = len(res)
                l -= 1
                r += 1
        return res
            
print(Solution().longestPalindrome("babad"))
print(Solution().longestPalindrome("cbbd"))
print(Solution().longestPalindrome("afkjsaasdffdsadower"))
print(Solution().longestPalindrome("afkjsaasdfyfdsadower"))