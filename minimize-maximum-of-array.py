class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        """
        first find the prefix sum of numbers 
        [3, 10, 11, 17]
        
        """
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        ans = nums[0]
        for i in range(1, len(nums) + 1):
            ans = max(ans, ceil(nums[i - 1] / i))
        return ans