class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for letter in s:
            if letter != "]":
                stack.append(letter)
            else:
                letters, num = [], ""
                while stack and stack[-1] != "[":
                    letters.append(stack.pop())
                stack.pop()
                
                while stack and stack[-1].isdigit():
                    num += stack.pop()
                    
                letters = "".join(letters[::-1])
                num = int(num[::-1])
                
                stack.append(letters*num)

        return "".join(stack)
            