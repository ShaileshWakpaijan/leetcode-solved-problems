# Leetcode 155

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        minVal = min(val, self.min[-1] if self.min else val)
        self.min.append(minVal)

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(10)
obj.push(5)
obj.push(20)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3, param_4)