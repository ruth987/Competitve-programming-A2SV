class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        
        for idx in range(n):
            nums.append(int(str(nums[idx])[::-1]))
        
        return len(set(nums))
    