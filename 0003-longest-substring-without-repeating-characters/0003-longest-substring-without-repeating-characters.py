class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        store = set()
        max_len = 0
        if s == "":
            return 0
        for right in range(len(s)):
            if s[right] not in store:
                store.add(s[right])
            else:
                max_len = max(max_len, right-left)
                while s[left] != s[right]:
                    store.remove(s[left])
                    left+=1
                left+=1
        max_len = max(max_len, right-left+1)
        return max_len
                
                    
            
            
