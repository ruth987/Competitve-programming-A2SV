class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        max_len = 0
        
        while right < len(nums):
            if nums[right]==0 and k>0:
                k-=1
            elif nums[right]==0 and k==0:
                max_len = max(max_len, right-left)
                while nums[left]==1:
                    left+=1
                left+=1
            right+=1
        max_len = max(max_len, right-left)    
        return max_len
                