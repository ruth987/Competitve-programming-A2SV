class Solution:
    def sortColors(self, nums):
        start, end = 0, len(nums)-1 #for zeros and twos.
        i = 0 # for the ones.
        
        def swap(nums, index1, index2):
            nums[index1], nums[index2] = nums[index2], nums[index1]
            return nums
        
        while i<=end:
            if nums[i] == 0:
                swap(nums, i, start)
                start += 1
            elif nums[i]==2:
                swap(nums, i, end)
                end-=1
                i-=1
            i += 1
        print(nums)
        

        
            
        