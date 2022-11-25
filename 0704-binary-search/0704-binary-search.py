class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        while left <= right:
            middlept = right-left+1//2
            if nums[middlept] == target:
                return middlept
            elif nums[middlept] > target:
                right = middlept-1
            else: #nums[middlept] < target
                left = middlept+1
        return -1
               
        
            
            