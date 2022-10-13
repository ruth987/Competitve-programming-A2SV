class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(n, idx1, idx2):
            n[idx1],n[idx2] = n[idx2], n[idx1]
            return n
        x = 0
        for index in range(len(nums)):
            if nums[index]!=0:
                swap(nums, x, index)
                x+=1