# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:

        n = mountain_arr.length()
        
        # Step 1: Find the peak of the mountain
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        
        peak = left
        
        # Step 2: Search in the left subarray
        left, right = 0, peak
        while left <= right:
            mid = (left + right) // 2
            mid_val = mountain_arr.get(mid)
            if mid_val == target:
                return mid
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        
        # Step 3: Search in the right subarray
        left, right = peak, n - 1
        while left <= right:
            mid = (left + right) // 2
            mid_val = mountain_arr.get(mid)
            if mid_val == target:
                return mid
            elif mid_val < target:
                right = mid - 1
            else:
                left = mid + 1
        
        # Step 4: If target is not found, return -1
        return -1