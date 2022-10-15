class Solution:
    def sortColors(self, nums):
        def swap(arr, index1, index2):
            arr[index1], arr[index2] = arr[index2], arr[index1]
            return arr
        
        left, right = 0, len(nums)-1
        i = 0 # a pointers to go through the array
        
        while i <= right:
            if nums[i]==0:
                swap(nums, i, left)
                left+=1
            elif nums[i]==2:
                swap(nums, i, right)
                right-=1
                i-=1
            i += 1
            
        return nums

        
            
        