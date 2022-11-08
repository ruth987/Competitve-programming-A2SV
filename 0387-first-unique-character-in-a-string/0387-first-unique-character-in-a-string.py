class Solution:
    def firstUniqChar(self, s: str) -> int:
        mydict = collections.Counter(s)
        
        for idx in range(len(s)):
            if mydict[s[idx]] == 1:
                return idx
        return -1
        