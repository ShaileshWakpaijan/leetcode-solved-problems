# class Solution:
#     def plusOne(self, digits):
#         return list(map(int, str(int("".join(map(str, digits))) + 1)))


class Solution:
    def plusOne(self, digits):  
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                if i == 0:
                    return [1] + digits
            else:
                digits[i] += 1
                break
        return digits
