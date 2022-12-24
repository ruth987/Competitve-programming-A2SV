class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        def swap(idx1, idx2, arr):
            arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
        
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] %2 == 0:
                left += 1
            elif nums[right] %2 != 0:
                right-=1
            elif nums[left] %2 != 0 and nums[right] %2 == 0:
                swap(left, right, nums)
                left += 1
                right -=1
            else:
                left += 1
        return nums
            