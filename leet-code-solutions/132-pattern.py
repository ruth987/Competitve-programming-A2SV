class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
      
        min_val = nums[0]
        stack = []

        for idx in range(1,len(nums)):
            while stack and nums[idx] >= stack[-1][0]:
                stack.pop() 

            if stack and nums[idx] > stack[-1][1]:
                return True

            stack.append([nums[idx], min_val])
            min_val = min(min_val, nums[idx])
        return False
        