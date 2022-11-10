class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = [] #monotonic increasing stack
        #k is the amount of integers we can pop from our stack
        
        for number in num:
            while stack and k > 0 and int(number) < int(stack[-1]):
                stack.pop()
                k-=1
            stack.append(number)
        stack = stack[:len(stack) - k]
        if not stack:
            return "0"
        return str(int("".join(stack)))
        