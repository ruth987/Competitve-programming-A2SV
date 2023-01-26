class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        start, end = 0, len(nums)-1
        count = 0
        
        while start < end:
            if nums[start]+nums[end] > k:
                end -= 1
            elif nums[start]+nums[end] < k:
                start += 1
            else:
                start += 1
                end -= 1
                count += 1
        return count