class Solution:
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        
        r, n = 0, len(needle) - 1

        for l in range(len(haystack)):
            if haystack[l] == needle[0]:
                r = l + n
                if haystack[l : r + 1] == needle:
                    return l
        return -1

        

print(Solution().strStr("hello", "ll"))
print(Solution().strStr("aaaaa", "bba"))
print(Solution().strStr("", ""))
print(Solution().strStr("abcmcbcdk", "bcd"))
print(Solution().strStr("abcmcbcdk", "kd"))