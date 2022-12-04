class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        how can we do it without extra space???

        """
        result = 0
        for n in nums:
            result = n^result
        return result
        
            
            