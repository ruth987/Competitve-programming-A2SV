class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        """
        append every openings
        when we find closings and stack[-1]=="("
            stack.pop()
            append the score
        when we find cloding and stack[-1].isdigit()
            newval = stack.pop()*2
            remove opeing
            then append newval
        at the end: return the sum of the stack
        
        """
        stack = []
        for ch in s:
            if ch == "(":
                stack.append(ch)
            else: # ch == ")"
                if stack[-1]=="(":
                    stack.pop()
                    stack.append(1)
                
                elif stack and str(stack[-1]).isdigit():
                    sum_ = 0
                    while stack and str(stack[-1]).isdigit():
                        sum_ += stack.pop()
                    if stack:
                        stack.pop()    
                    newscore = sum_*2
                    stack.append(newscore)
            # print(stack)
        return sum(stack)
    
                    
        