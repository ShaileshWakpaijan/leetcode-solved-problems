# Leetcode 141

class Solution:
    def hasCycle(self, head):
    #     occurs = set()
    #     crr = head
    #     while crr:
    #         if crr in occurs:
    #             return True
    #         occurs.add(crr)
    #         crr = crr.next
    #     return False

        ##### Using Floyd's Tortoise and Hare Algorithm #####
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if slow == fast:
                return True
        return False
