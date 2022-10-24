class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        max_sum = 0
        for idx in range(len(nums)):
            if idx % 2 != 0:
                max_sum += nums[idx]
                
        return max_sum
            