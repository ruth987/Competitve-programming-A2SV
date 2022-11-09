class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
            stack, p_idx = [], 0
            
            for num in pushed:
                stack.append(num)
                while stack and p_idx<len(popped) and stack[-1] == popped[p_idx]:
                    stack.pop()
                    p_idx += 1

            if stack:
                return False
            return True
        
            