class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def search(x):
            left, right = 0, len(nums)
            while left < right:
                mid = (left+right) //2
                if nums[mid] < x:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        left_most = search(target)
        right_most = search(target+1) -1
        if left_most <= right_most:
            return [left_most, right_most]
        return [-1, -1]
        
