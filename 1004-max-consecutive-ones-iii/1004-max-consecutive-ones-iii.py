class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len, zeros = 0, 0
        left = 0
        
        for right in range(len(nums)):
            if nums[right] == 0 and zeros<k:
                zeros+=1
            elif nums[right] == 0 and zeros == k:
                max_len = max(max_len, right-left)
                while nums[left] != 0:
                    left+=1
                left+=1
        max_len = max(max_len, right-left+1)
        return max_len