# Leetcode 19

class Solution:
    def removeNthFromEnd(self, head, n):
        # count nodes
        length = 0
        crr = head
        while crr:
            length += 1
            crr = crr.next
        
        if length == 1:
            return None
        
        # previous node of item to be delete
        itemAt = length - n
        if itemAt == 0:
            return head.next

        crr = head

        # traverse to previous node
        for i in range(1, itemAt):
            crr = crr.next
        
        # deleting the node
        if crr.next:
            crr.next = crr.next.next
        else:
            crr.next = None
        return head
