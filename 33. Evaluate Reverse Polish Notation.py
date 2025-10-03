# Leetcode 150

class Solution:
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token in "+-*/":
                n1 = stack.pop()
                n2 = stack.pop()
                if token == "+":
                    stack.append(n2 + n1)
                elif token == "-":
                    stack.append(n2 - n1)
                elif token == "*":
                    stack.append(n2 * n1)
                elif token == "/":
                    stack.append(int(n2 / n1))
            else:
                stack.append(int(token))

        return stack[-1]

print(Solution().evalRPN(["2","1","+","3","*"]))
print(Solution().evalRPN(["4","13","5","/","+"]))
print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
