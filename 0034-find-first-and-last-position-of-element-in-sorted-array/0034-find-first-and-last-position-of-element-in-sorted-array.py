class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        return [the first time u see target, the last time you see target]
        
        """
        left, right = 0, len(nums)-1
        # nums = ["x"]+nums+["x"]
        
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                start, end  = mid, mid
                while end < len(nums) and nums[end] == target:
                    end += 1
                while start>=0 and start < len(nums) and nums[start] == target:
                    start -= 1
                return [start+1, end-1]
            
            elif nums[mid] > target:
                right = mid-1
                
            else:
                left = mid+1
            
        return [-1,-1]
    