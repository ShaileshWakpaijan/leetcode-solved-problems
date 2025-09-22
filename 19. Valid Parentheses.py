class Solution:
    def isValid(self, s):
        stack = []
        brackets = { ")" : "(", "]" : "[", "}" : "{" }
        for itm in s:
            if itm in brackets.values():
                stack.append(itm)
            else:
                if stack and stack[-1] == brackets[itm]:
                    stack.pop()
                else:
                    return False
        else:
            if len(stack):
                return False
            return True

print(Solution().isValid("{(()[{({([])}[{}])}])}"))
