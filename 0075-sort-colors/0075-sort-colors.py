class Solution:
    def sortColors(self, nums):
        ones, twos, zeros = 0, 0, 0
        
        for number in nums:
            if number == 0:
                zeros += 1
            elif number == 1:
                ones += 1
            else:
                twos += 1
                
        for idx in range(len(nums)):
            if idx < zeros:
                nums[idx] = 0
            elif idx >= zeros and idx < zeros+ones:
                nums[idx] = 1
            else:
                nums[idx] = 2
            
            
        