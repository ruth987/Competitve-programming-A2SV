class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        #apply the first operations
        stack = [nums[0]]
        here = 0
        for idx in range(1,len(nums)):
            if nums[idx]==nums[idx-1] and here == 0:
                stack.pop()
                stack.append(nums[idx]*2)
                stack.append(0)
                here = 1
            else:
                here = 0
                stack.append(nums[idx])
        #put zeros at the end
        x = 0
        for idx in range(len(stack)):
            if stack[idx]!=0:
                stack[idx], stack[x] = stack[x], stack[idx]
                x += 1
        return stack
        