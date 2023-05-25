class Solution:
    def minDifference(self, nums: List[int]) -> int:
        """
        one move : pick one number then change to other number

        """
        if len(nums) <= 3:
            return 0
        start = 0
        end = len(nums)-4
        n = len(nums)
        nums.sort()
        min_diff = float('inf')
        while start < n and end < n:
            diff = nums[end]-nums[start]

            if diff < min_diff:
                min_diff = diff
                x, y = start, end
            start += 1
            end += 1
        return min_diff