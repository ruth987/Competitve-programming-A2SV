class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        left, right = 0, 1
        while right < len(nums):
            if nums[left] == 0:
                while right < len(nums) and nums[right] == 0:
                    right+=1
                if right < len(nums):
                    nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right+=1
        
        