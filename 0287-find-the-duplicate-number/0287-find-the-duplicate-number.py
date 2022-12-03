class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        we can simply do this problem using o(n) space complexity but the triccky part 
        is how can we do it using o(1) space complexity??
        
        so how can we do it without using extra space?
        this approach makes the time complexity a little slower because we are sorting
        the array but the space complexity becomes constant times.
        
        """
        nums.sort()
        
        for idx in range(1, len(nums)):
            if nums[idx]==nums[idx-1]:
                return nums[idx]
            
        