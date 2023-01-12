class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        n = len(strs[0])
        the_strings = []
        
        for idx in range(n):
            for index in range(1,len(strs)):
                if strs[index][idx]<strs[index-1][idx]:
                    count += 1
                    break
                
        return count 
            
            