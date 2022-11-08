class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for letter in s:
            x = 0
            if stack and letter.isupper() and stack[-1]==letter.lower():
                x = 1
                stack.pop()
                
            if stack and letter.islower() and stack[-1]==letter.upper():
                x = 1
                stack.pop()
                
            if x == 0:
                stack.append(letter)
                
        return "".join(stack)
        