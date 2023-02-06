class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        start, middle = 0, n
        output = []
        
        while middle < len(nums):
            output.append(nums[start])
            output.append(nums[middle])
            start += 1
            middle += 1
        
        return output
            