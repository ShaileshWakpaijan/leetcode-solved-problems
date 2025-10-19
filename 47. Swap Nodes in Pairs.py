# Leetcode 24

class Solution:
    def swapPairs(self, head):
        if not head:
            return None
        if not head.next:
            return head

        return self.swapTwoNode(head, head.next, head.next.next)
    
    def swapTwoNode(self, prev, crr, next = None):
        if not crr:
            return prev

        prev.next = next
        crr.next = prev

        if not next or not next.next:
            return crr
        prev.next = self.swapTwoNode(next, next.next, next.next.next)
        return crr