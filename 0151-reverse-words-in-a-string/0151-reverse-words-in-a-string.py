class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        start, end = 0, len(s)-1
        
        while start<end:
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start += 1
            end -= 1
        return ' '.join(s)