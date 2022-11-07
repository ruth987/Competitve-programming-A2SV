class Solution:
    def longestWPI(self, hours: List[int]) -> int: 
        prefixSum=0
        hmap={}
        ans=0
        
        for length,hour in enumerate(hours):
            prefixSum+=1 if hour>8 else -1
            if prefixSum>0:ans=max(ans,length+1)
            if prefixSum not in hmap:
                hmap[prefixSum]=length
            if prefixSum-1 in hmap:
                ans=max(ans,length-hmap[prefixSum-1])
        return ans
   