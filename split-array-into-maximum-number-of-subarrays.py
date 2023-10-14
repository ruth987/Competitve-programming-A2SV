class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        min_val = nums[0]

        for i in range(len(nums)):
            min_val &= nums[i]

        if min_val > 0:
            return 1

        last = 0
        val = nums[0]
        part = 0
        i = 0
        for i in range(len(nums)):
            val &= nums[i]
            if val == min_val:
                part += 1
                if i+1 < len(nums):
                    val = nums[i+1]

        # if val == min_val:

        
        return part