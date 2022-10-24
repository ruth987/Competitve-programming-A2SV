class Solution:
    def isPalindrome(self, s: str) -> bool:
        slist = []
        for ch in s:
            if ch.isalpha() or ch.isdigit():
                slist.append(ch.lower())
        return slist == slist[::-1]
                