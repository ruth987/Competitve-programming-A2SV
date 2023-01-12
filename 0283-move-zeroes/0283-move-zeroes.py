class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for idx in range(len(nums)):
            if nums[idx] != 0:
                nums[idx], nums[i] = nums[i], nums[idx]
                i+=1
                
                