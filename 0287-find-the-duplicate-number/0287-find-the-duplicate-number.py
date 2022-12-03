class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        we can simply do this problem using o(n) space complexity but the triccky part 
        is how can we do it using o(1) space complexity??
        """
        seen = set()
        
        for num in nums:
            if num not in seen:
                seen.add(num)
            else: # if num in seen
                return num
            