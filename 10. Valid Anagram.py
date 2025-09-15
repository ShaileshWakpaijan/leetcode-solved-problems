class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        l1 = list(map(ord, s))
        l1.sort()
        l2 = list(map(ord, t))
        l2.sort()
        
        for i in range(len(l1)):
            if l1[i] != l2[i]:
                return False
        else:
            return True