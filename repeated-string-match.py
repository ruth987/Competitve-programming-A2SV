class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n, m = len(b)//len(a), len(b)%len(a)

        if m:
            n += 1
        if b in a * n:
            return n
        elif b in a * (n+1):
            return n+1
        else:
            return -1