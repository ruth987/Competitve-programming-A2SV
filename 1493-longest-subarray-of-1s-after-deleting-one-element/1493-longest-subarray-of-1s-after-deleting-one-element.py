class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, right = 0, 0
        max_len, count = 0, 0 
        
        while right < len(nums): 
            if nums[right]==0 and count == 1:
                max_len = max(max_len, right-left-1)
                while nums[left]!=0:
                    left+=1
                left+=1
            elif nums[right]==0:
                count +=1 
            right+=1
        max_len = max(max_len, right-left-1)
        return max_len