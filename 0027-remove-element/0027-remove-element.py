class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        next_element = 0  
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[next_element] = nums[i]
                next_element += 1
        
        return next_element
            
                