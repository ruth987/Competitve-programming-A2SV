class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        mydict = {}
        presum = 0
        ans = 0
        
        for idx in range(len(nums)):
            if presum not in mydict:
                mydict[presum] = 1
            else:
                mydict[presum] += 1
            
            presum += nums[idx]
            if presum - goal in mydict:
                ans += mydict[presum-goal]
                
        return ans
                       