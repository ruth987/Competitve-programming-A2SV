class Solution:
    def sortColors(self, nums):
        start, end = 0, len(nums)-1
        i = 0 # the index that goes through the array
        
        while i <= end:
            if nums[i] == 0:
                nums[i], nums[start] = nums[start], nums[i]
                start+=1
            elif nums[i] == 2:
                nums[i], nums[end] = nums[end], nums[i]
                end-=1
                i-=1
            i+=1                            
        print(nums)

            
        
        