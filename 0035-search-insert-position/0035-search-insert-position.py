class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        while left<=right:
            mid = right-left+1//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        if target < nums[0]:
            return 0
        return mid+1
                
            