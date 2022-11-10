class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #prefix sum
        for idx in range(1, len(nums)):
            nums[idx] += nums[idx-1]
        nums = [0]+nums
        
        left, right = 1, 1
        min_len = len(nums)+1
        
        while right < len(nums):
            while nums[right]-nums[left-1] >= target:
                min_len = min(min_len, right-left+1)
                left+=1
            right+=1
        if min_len == len(nums)+1:
            return 0
        return min_len
        
                
                
                
                
                
                
                
                
                
            
            