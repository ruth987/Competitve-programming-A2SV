class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        nums = is a sorted array.
        target= is the number we are searching for.
        
        if we find the target then return the index else return -1
        
        so the binary search algorithm time comp: o(log n)
        
        the brute force approach is going through all the elements of the array.
        the time comp: o(n)
        space comp: o(1)
        """
        for idx in range(len(nums)):
            if nums[idx] == target:
                return idx
        return -1
        