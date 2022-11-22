class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left, i = 0, 0
        
        while left < len(haystack):
            output = left
            count = 0
            while left<len(haystack) and haystack[left]==needle[i] and i<len(needle):
                count +=1
                left+=1
                i+=1
                if i == len(needle):
                    return output
            i = 0
            left-=count
            left+=1
            
        return -1
        
        
        