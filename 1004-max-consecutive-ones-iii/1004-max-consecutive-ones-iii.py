class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, max_len = 0, 0
        
        for right in range(len(nums)):
            if nums[right]==0 and k>0:
                k-=1
            elif nums[right]==0 and k==0:
                max_len = max(max_len, right-left)
                while nums[left]==1:
                    left+=1
                left+=1

        max_len = max(max_len, right-left+1)    
        return max_len
                