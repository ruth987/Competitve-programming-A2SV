class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == s[::-1]:
            return 1
        mydict = collections.Counter(s)
        return len(mydict)