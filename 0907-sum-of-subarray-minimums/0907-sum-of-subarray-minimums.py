class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = [-1, 0]
        sum_ = 0
        
        for idx in range(1, len(arr)):
            while len(stack) >= 2 and arr[idx] < arr[stack[-1]]:
                sum_ += abs((idx-stack[-1])*(stack[-1]-stack[-2]))* arr[stack[-1]]
                stack.pop()
                
            stack.append(idx)
            
        stack.append(len(arr))

        for i in range(1, len(stack)-1):
            sum_ += ((stack[i]-stack[i-1])*(len(arr) -stack[i]))*arr[stack[i]]
        
        return sum_%(10**9 + 7)
