class Solution:
    def isPalindrome(self, s):
        s1 = "".join(c for c in s.lower() if c.isalnum())
        return s1 == s1[::-1]
    
        ############## Another approach ##############
        # for i in range(1, len(s1) + 1):
        #     if s1[i - 1] != s1[-i]:
        #         return False
        # else:
        #     return True



str1 = "Was it a car or a cat I saw?"
str2 = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(str1))
print(Solution().isPalindrome(str2))
