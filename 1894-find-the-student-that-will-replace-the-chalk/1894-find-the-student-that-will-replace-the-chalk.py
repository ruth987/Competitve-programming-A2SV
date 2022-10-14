class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s = sum(chalk)
        i = 0
        check = 0
        l = len(chalk)
        
        if l == 1:
            return 0
        
        while k >= (s)**2:
            k -= (s**2)
            
        while k >= (s) and k != 1:
            k -= s 
            check = 1
            
        while chalk[i] <= k and  k != 0:
            k -= chalk[i]
            i += 1
            check = 1
            
        return i if check else 0
        