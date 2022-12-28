class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        aset = set(nums)
        
        for num in range(len(nums)+1):
            if num not in aset:
                return num
            