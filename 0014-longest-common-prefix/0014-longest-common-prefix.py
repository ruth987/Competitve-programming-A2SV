class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        
        for word in strs:
            if first > word:
                first = word
                
        last = strs[0]
        
        for word in strs:
            if last < word:
                last = word
        print(first, last)
        ans = ""
        i, j = 0, 0
        if len(strs) == 1:
            return strs[0]
        while i<len(first) and j<len(last) and first[i] == last[j]:
            ans += first[i]
            i+=1
            j+=1
        return ans
        
        