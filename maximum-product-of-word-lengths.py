class Solution:
    def maxProduct(self, words: List[str]) -> int:

        bit_rep = [0]*len(words)
        for i in range(len(words)):
            for l in words[i]:
                bit_rep[i] |= (1 << (ord(l) - 97))
        ans = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if bit_rep[i] & bit_rep[j] == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans