class Solution:
    def findPivot(self,nums):
            start=0
            end = len(nums)-1

            while start< end:
                mid = start+(end-start)//2
                if nums[mid]>nums[mid+1] and mid<=end:
                    return mid  
                if nums[mid]<nums[mid-1]:
                    return mid-1
                if nums[start]>=nums[mid]:
                    end = mid-1
                else:
                    start=mid+1

            return -1


    def binarySearch(self,arr,target,start,end):
        while (start<=end):   
            mid= start+(end-start)//2
            if target==arr[mid] :
                return mid
            elif target < arr[mid]:
                end=mid-1
            else:
                start= mid+1
        return -1  
            

    def search(self, nums, target):
        pivot=self.findPivot(nums)                  
        if pivot==-1:                             
            return self.binarySearch(nums,target,0,len(nums)-1)
        if nums[pivot]==target:
            return pivot
        elif target>=nums[0]:                 
            return self.binarySearch(nums,target,0,pivot-1)
        else:                                     
            return self.binarySearch(nums,target,pivot+1,len(nums)-1) 