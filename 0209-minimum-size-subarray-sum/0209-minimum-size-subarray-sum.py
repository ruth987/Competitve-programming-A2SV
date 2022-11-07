class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len, summ = len(nums)+1, 0
        left, right = 0, 0
        
        while right < len(nums):
            summ += nums[right]
            if summ >= target:
                min_len = min(min_len, right-left+1)
                while summ >= target:
                    if summ-nums[left] >= target:
                        summ-=nums[left]
                        left+=1
                        min_len = min(min_len, right-left+1)    
                    else:
                        break    
            right+=1
            
        if min_len == len(nums)+1:
            return 0
        return min_len
        
