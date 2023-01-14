class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        stack = [nums[0]]
        
        for idx in range(1,len(nums)):
            if nums[idx] != stack[-1]:
                stack.append(nums[idx])
            else: # if it is the same
                element = stack.pop()
                stack.append(2*element)
                stack.append(0)
        
        #move zeros
        i = 0
        for index in range(len(stack)):
            if stack[index]!=0:
                stack[i], stack[index] = stack[index], stack[i]
                i += 1
        return stack
     