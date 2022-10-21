class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        
        for ops in operations:
            if ops.lstrip("-").isdigit():
                stack.append(int(ops))
            else:
                if ops== "C":
                    stack.pop()
                elif ops == "D":
                    stack.append(2*int(stack[-1]))
                else: # ops == "+"
                    if len(stack) >=2:
                        stack.append(int(stack[-1])+int(stack[-2]))
                    
        return sum(stack)
                    