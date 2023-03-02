class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        l = len(nums)
        ans = [-1]*l
        nums = nums+nums
        stack = []
        
        for idx in range(len(nums)):
            while stack and nums[idx] > nums[stack[-1]]:
                i = stack.pop()
                ans[i%l] = nums[idx]

            stack.append(idx)
 
        return ans
        
        