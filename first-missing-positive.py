class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        find and return the smallest missing positive integer
        """
        adict = {}
        for num in nums:
            if num not in adict:
                adict[num] = 1
        
        for idx in range(1, len(nums)+1):
            if idx not in adict:
                return idx
        
        return len(nums)+1