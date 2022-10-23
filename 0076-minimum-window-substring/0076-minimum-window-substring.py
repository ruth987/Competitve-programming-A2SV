class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        def isMatch(s1,s2): return all([s2[c]>=s1[c] for c in s1.keys()])
        t=Counter(t)
        curr,res= s[:len(t)-1],""
        currSet=Counter([c for c in curr if c in t])
        for c in s[len(t)-1:]:
            curr+=c
            if c in t:  
                currSet[c]+=1
                if currSet[c] >= t[c] and isMatch(t,currSet):
                    while True:
                        if curr[0] in currSet:
                            if currSet[curr[0]]==t[curr[0]]:
                                break
                            currSet[curr[0]]-=1
                        curr=curr[1:]
                    if not res or len(res)>len(curr):
                        res=curr
        return res