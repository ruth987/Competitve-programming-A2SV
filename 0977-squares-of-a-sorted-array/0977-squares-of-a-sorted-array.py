class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        what is the most obvious approach??
        1, squaring all the elements
        2, returning the sorted array of the squares 
        we can do this in different ways?
        - sort built in function 
        - using some other sorting algorithms
        
        """
        for idx in range(len(nums)):
            nums[idx] = nums[idx]**2
        #print(nums)
        return sorted(nums)
        