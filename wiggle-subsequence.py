class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """
            [17,5,10,13,15,10]
            
            [1, 1, 3, 3, 3, 0]
            [1, 2, 2, 2, 2, 0]
        
        
        """
        n = len(nums)
        
        @cache
        def dp(idx, prev, direc):
            
            if idx == n:
                return 0
            
            if prev == None:
                choice1 = dp(idx+1, idx, True) + 1
                choice2 = dp(idx + 1, idx, False) + 1
                choice3 = dp(idx + 1, prev, direc)
                
                return max(choice1, choice2, choice3)
            
            else:
                if direc and nums[idx] > nums[prev]:
                    choice1 = dp(idx+1, idx, not direc) + 1
                    choice2 = dp(idx + 1, prev, direc)
                    
                    return max(choice1, choice2)
                elif not direc and nums[idx] < nums[prev]:
                    choice1 = dp(idx+1, idx, not direc) + 1
                    choice2 = dp(idx + 1, prev, direc)
                    
                    return max(choice1, choice2)
                else:
                    return dp(idx + 1, prev, direc)
        
        return dp(0, None, True)