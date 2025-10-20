# Leetcode 82. Remove Duplicates from Sorted List II

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return
        if not head.next:
            return head

        dummy = ListNode(next = head)
        ptr1 = dummy
        ptr2 = head.next

        while ptr2:
            if ptr1.next.val != ptr2.val:
                ptr1 = ptr1.next
            else:
                while ptr2.next and ptr2.val <= ptr1.next.val:
                    ptr2 = ptr2.next
                if not ptr2.next and ptr2.val == ptr1.next.val:
                    ptr1.next = None
                    break
                else:
                    ptr1.next = ptr2
            ptr2 = ptr2.next

        return dummy.next