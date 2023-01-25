class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mydict = {}
        
        for idx in range(len(s)):
            if s[idx] not in mydict :
                mydict[s[idx]] = idx
            elif s[idx] in mydict and idx > mydict[s[idx]]:
                mydict[s[idx]] = idx
                
        left, right = 0, 0
        ans = []
        while right < len(s):
            n = mydict[s[right]]
            while right < n:
                if mydict[s[right]] > n:
                    n = mydict[s[right]]
                right+=1

            ans.append(right-left+1)
            left = right+1
            right+=1
        return ans
            

