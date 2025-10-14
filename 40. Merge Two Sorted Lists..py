# Leetcode 21


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
LL.insert_at_last(2)
LL.insert_at_last(4)
LL.print_list()
print()
LL2 = SLL()
LL2.insert_at_last(1)
LL2.insert_at_last(3)
LL2.insert_at_last(4)
LL2.print_list()
print()

# class Solution:
#     def mergeTwoLists(self, list1 = None, list2 = None):
#         dummy = crr = ListNode()

#         while list1 and list2:
#             if list1.val < list2.val:
#                 crr.next = list1
#                 list1 = list1.next
#             else:
#                 crr.next = list2
#                 list2 = list2.next

#             crr = crr.next
        
#         crr.next = list1 or list2
#         return dummy.next


########## Using Recursion ##########
class Solution:
    def mergeTwoLists(self, list1 = None, list2 = None):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

Solution().mergeTwoLists(LL.start, LL2.start)
LL.print_list()
print()
LL2.print_list()
