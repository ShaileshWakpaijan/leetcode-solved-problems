# Leetcode 12
class Solution:
    def intToRoman(self, num):
        mapping = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }

        a = str(num)
        res = ""
        arr = []
        numLen = len(a)
        for i in range(numLen):
            arr.append(a[i] + "0"*(numLen - i - 1))

        for i in range(numLen):
            power = 10**(numLen - i - 1)
            n = int(int(arr[i])/power)
            if n == 0:
                continue
            elif n == 4:
                n += 1
                res += mapping[power] + mapping[5 * power]
            elif n == 9:
                n += 1
                res += mapping[power] + mapping[10 * power]
            elif n < 5:
                res += mapping[power] * n
            else:
                res += mapping[5*power] + mapping[power] * (n - 5)

        return res


print(Solution().intToRoman(3749))
print(Solution().intToRoman(58))
print(Solution().intToRoman(1994))