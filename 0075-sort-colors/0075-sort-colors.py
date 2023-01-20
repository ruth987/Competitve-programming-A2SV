class Solution:
    def sortColors(self, nums):
        i = 0
        start, end = 0, len(nums)-1
        
        while i <= end:
            if nums[i] == 0:
                nums[start], nums[i] = nums[i], nums[start]
                start += 1
            elif nums[i] == 2:
                nums[end], nums[i] = nums[i], nums[end]
                end -= 1
                i -= 1
            i += 1

        print(nums)