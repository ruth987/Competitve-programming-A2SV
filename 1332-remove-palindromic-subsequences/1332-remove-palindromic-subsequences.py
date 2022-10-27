class Solution:
     def removePalindromeSub(self, s):
        if s == s[::-1]:
            return 1
        first = s[0]
        for letter in s:
            if letter != first:
                return 2
        return 1