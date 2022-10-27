class Solution:
    def removeDuplicates(self, nums):
        idx = 0
        for number in nums:
            if idx < 2 or number > nums[idx-2]:
                nums[idx] = number
                idx += 1
        return idx
                
