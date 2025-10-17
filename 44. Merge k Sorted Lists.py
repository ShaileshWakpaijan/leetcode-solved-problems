# Leetcode 23

class ListNode:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

class SLL:
    def __init__(self, start = None):
        self.start = start
    
    def is_empty(self):
        return self.start == None

    def insert_at_last(self, data):
        n = ListNode(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n

    def search(self, data):
        temp = self.start
        while temp.next is not None:
            if temp.val == data:
                return temp
            temp = temp.next
        return None

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.val, end = " ")
            temp = temp.next

LL = SLL()
LL.insert_at_last(1)
LL.insert_at_last(4)
LL.insert_at_last(5)
LL.print_list()
print()
LL2 = SLL()
LL2.insert_at_last(1)
LL2.insert_at_last(3)
LL2.insert_at_last(4)
LL2.print_list()
print()
LL3 = SLL()
LL3.insert_at_last(2)
LL3.insert_at_last(6)
LL3.print_list()
print()

class Solution:
    def mergeKLists(self, lists):
        l = len(lists)
        if l == 0:
            return None
        
        for i in range(1, l):
            lists[i] = self.merge2List(lists[i - 1], lists[i])
        
        return lists[-1]
    
    def merge2List(self, l1, l2):
        dummy = crr = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                crr.next = l1
                l1 = l1.next
            else:
                crr.next = l2
                l2 = l2.next
                
            crr = crr.next
        crr.next = l1 or l2
        return dummy.next




res = Solution().mergeKLists([LL.start, LL2.start, LL3.start])
LL.print_list()
print()
LL2.print_list()
print()
LL3.print_list()
