class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        left, right, x = 0, 1, 0
        max_diff = 0
        while right < len(nums):
            if nums[right]<=nums[left]:
                left = right
            else:
                x = 1
                max_diff = max(max_diff, nums[right]-nums[left])
            right+=1
        if x == 1:
            return max_diff
        return -1
