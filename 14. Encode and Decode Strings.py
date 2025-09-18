class Solution:
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s):
        i = 0
        arr = []
        while i < len(s):
            j = int(s[i])
            arr.append(s[i + 2:i +j + 2])
            i = i + 2+ j
        return(arr)


ss = ["we","say",":","yes"]

a = Solution()
r = a.encode(ss)
print("r", r)
print(a.decode(r))