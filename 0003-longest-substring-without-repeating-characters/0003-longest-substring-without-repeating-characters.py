class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        chs = set()
        max_len = 0
        
        while right < len(s):
            if s[right] not in chs:
                chs.add(s[right])
            else: #if it is in the chs
                max_len = max(max_len, right-left)
                while s[left] != s[right]:
                    chs.remove(s[left])
                    left+=1
                left+=1
            right +=1 
        max_len = max(max_len, right-left)
        return max_len
                