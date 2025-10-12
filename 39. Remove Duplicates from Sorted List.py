# Leetcode 83

class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return head
        
        temp = head
        while temp:
            if temp.next and temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head
