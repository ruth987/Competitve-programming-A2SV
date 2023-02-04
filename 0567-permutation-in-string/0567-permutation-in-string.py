class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mydict = collections.Counter(s1)
                
        left, right = 0, len(s1)
        while right < len(s2)+1:
            yourdict = collections.Counter(s2[left:right])
            if mydict == yourdict:
                return True
            else:
                left+=1
                right+=1
        return False