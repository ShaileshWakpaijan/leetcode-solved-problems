class Solution:
    def groupAnagrams(self, strs):
        res = {}
        for crr in strs:
            temp = "".join(sorted(crr))
            if temp in res.keys():
                res[temp].append(crr)
            else:
                res[temp] = [crr]
        return list(res.values())

print(Solution().groupAnagrams(["act","pots","tops","cat","stop","hat"]))
