# LeetCode 3461

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        length = len(s)
        while length > 2:
            s = "".join(str((int(s[i]) + int(s[i + 1])) % 10) for i in range(length - 1))

            length = len(s)
            
        if length == 2 and s[0] == s[1]:
            return True
        return False