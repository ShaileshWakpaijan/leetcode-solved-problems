# Leetcode 206
class Solution:
    def reverseList(self, head):
        prev, crr = None, head

        while crr:
            temp = crr.next
            crr.next = prev
            prev = crr
            crr = temp
        return prev
