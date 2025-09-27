#Leetcode 567
class Solution:
    def checkInclusion(self, s1, s2):
        l, r = 0, len(s1)
        
        while r <= len(s2):
            if sorted(s2[l : r]) == sorted(s1):
                return True
            else:
                r += 1
                l += 1
                
        return False
    

print(Solution().checkInclusion("ab", "eidbaooo"))
print(Solution().checkInclusion("ab", "eidboaoo"))
