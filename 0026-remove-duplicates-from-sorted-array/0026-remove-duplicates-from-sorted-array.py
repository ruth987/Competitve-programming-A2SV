class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        idx = 1
        while idx < len(nums):
            number = nums[idx-1]
            while idx < len(nums) and nums[idx] == number:
                count += 1
                nums[idx] = "_"
                idx +=1
            idx += 1
        
        i = 0
        for idx in range(len(nums)):
            if nums[idx] != "_":
                nums[i] = nums[idx]
                i += 1

        return len(nums)-count 