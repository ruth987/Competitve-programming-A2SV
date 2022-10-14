class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sum_chalk = sum(chalk)
        remainder = k%sum(chalk)
        if remainder == 0:
            return 0
        else:
            ans = idx = x = 0
            while remainder >= chalk[idx]:
                x = 1
                remainder -= chalk[idx]
                ans = idx
                if idx == len(chalk)-1:
                    idx = 0
                else:
                    idx+=1
                    
            if x==0 or ans == len(chalk)-1:
                return 0
            return ans+1
            
    
                