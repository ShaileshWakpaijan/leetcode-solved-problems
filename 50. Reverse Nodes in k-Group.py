# LeetCode Problem 25: Reverse Nodes in k-Group

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        if not head:
            return None
        temp = head

        # Check if there are at least k nodes to reverse
        for i in range(k - 1):
            if not temp or not temp.next:
                return head
            temp = temp.next

        nextHead = temp.next if temp.next else None # Store the head of the next segment
        temp.next = None
        self.reverseList(head) # Reverse the first k nodes
        
        restListHead = self.reverseKGroup(nextHead, k) # Reverse the remaining list
        head.next = restListHead # Connect the reversed part with the rest of the list

        return temp
    
    # Helper function to reverse a linked list
    def reverseList(self, head):
        prev, crr = None, head
        while crr:
            temp = crr.next
            crr.next = prev
            prev = crr
            crr = temp
