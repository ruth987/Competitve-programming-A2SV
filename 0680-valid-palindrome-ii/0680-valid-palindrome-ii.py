class Solution:
    def validPalindrome(self, s: str) -> bool:
        count = 0
        start, end = 0, len(s)-1
        
        while start <= end:
            if s[start] != s[end]:
                option1 = s[0:start]+s[start+1:]
                option2 = s[0:end]+s[end+1:]
                if option1 == option1[::-1] or option2 ==option2[::-1]:
                    return True
                else:
                    return False
            start+=1
            end-=1
            
        return True