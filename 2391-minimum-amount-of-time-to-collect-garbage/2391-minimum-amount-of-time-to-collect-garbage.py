class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        l,m,p,g,res=0,0,0,0,0
        for i in range(len(garbage)):
            if 'M' in garbage[i] and m<i:
                m=i
            if 'P' in garbage[i] and p<i:
                p=i
            if 'G' in garbage[i] and g<i:
                g=i
            l+=len(garbage[i])
            
        if m!=0:
            res=sum(travel[:m])
        if p!=0:
            res+=sum(travel[:p])
        if g!=0:
            res+=sum(travel[:g])
            
        return res+l