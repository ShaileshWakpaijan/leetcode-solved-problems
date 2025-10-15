# Leetcode 141

class Solution:
    def hasCycle(self, head):
        occurs = set()
        crr = head
        while crr:
            if crr in occurs:
                return True
            occurs.add(crr)
            crr = crr.next
        return False
