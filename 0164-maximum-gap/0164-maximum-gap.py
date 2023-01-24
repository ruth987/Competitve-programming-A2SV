class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        nums.sort()
        max_diff = 0
        
        for idx in range(1, len(nums)):
            max_diff = max(max_diff, nums[idx]-nums[idx-1])
            
        return max_diff