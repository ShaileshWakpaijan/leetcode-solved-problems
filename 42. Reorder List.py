# Leetcode 143

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
LL.insert_at_last(3)
LL.insert_at_last(4)
LL.insert_at_last(5)
LL.print_list()
print()

class Solution:
    def reorderList(self, head):
        arr = []
        crr = head
        while crr:
            arr.append(crr)
            crr = crr.next

        while arr:
            if len(arr) > 2:
                arr[0].next = arr[-1]
                arr[-1].next = arr[1]
                arr.pop(0)
            elif len(arr) == 2:
                arr[0].next = arr[-1]
                arr[-1].next = None
                arr.pop(0)
            else:
                arr[0].next = None
            arr.pop()

Solution().reorderList(LL.start)
LL.print_list()