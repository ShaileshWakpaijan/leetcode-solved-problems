# Leetcode 2
 
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
LL.insert_at_last(2)
LL.insert_at_last(4)
LL.insert_at_last(3)
LL.print_list()
print()
LL2 = SLL()
LL2.insert_at_last(5)
LL2.insert_at_last(6)
LL2.insert_at_last(4)
LL2.print_list()
print()

LL3 = SLL()
LL3.insert_at_last(9)
LL3.insert_at_last(9)
LL3.insert_at_last(9)
LL3.insert_at_last(9)
LL3.insert_at_last(9)
LL3.print_list()
print()
LL4 = SLL()
LL4.insert_at_last(9)
LL4.insert_at_last(9)
LL4.print_list()
print()

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = prev = ListNode()
        temp = 0
        while l1 or l2 or temp:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            value = v1 + v2 + temp
            temp = value // 10
            prev.next = ListNode(value % 10)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            prev = prev.next

        return dummy.next
    
sol = Solution().addTwoNumbers(LL.start, LL2.start)
while sol is not None:
    print(sol.val, end = " ")
    sol = sol.next

print()

sol2 = Solution().addTwoNumbers(LL3.start, LL4.start)
while sol2 is not None:
    print(sol2.val, end = " ")
    sol2 = sol2.next