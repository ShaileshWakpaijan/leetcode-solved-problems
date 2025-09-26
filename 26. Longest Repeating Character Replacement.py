class Solution:
    def characterReplacement(self, s, k):
        # freq = {}
        # res = 0
        # l = 0
        # for r in range(len(s)):
        #     rItem = s[r]
        #     freq[rItem] = 1 + freq.get(rItem, 0)

        #     while (r - l + 1) - max(freq.values()) > k:
        #         freq[s[l]] -= 1
        #         l += 1

        #     res = max(res, r - l + 1)
        
        # return res

        ####### Optimized max calculation #######
        freq = {}
        res = 0
        l = 0
        maxF = 0
        for r in range(len(s)):
            rItem = s[r]
            freq[rItem] = 1 + freq.get(rItem, 0)
            maxF = max(maxF, freq[rItem])

            if (r - l + 1) - maxF > k:
                freq[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        
        return res


print(Solution().characterReplacement("AABABBA", 1))
print(Solution().characterReplacement("ABAB", 2))
print(Solution().characterReplacement("KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF", 4))