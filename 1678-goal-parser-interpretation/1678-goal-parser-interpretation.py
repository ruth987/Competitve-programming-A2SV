class Solution:
    def interpret(self, command: str) -> str:
        """
        we can use a stack: 
        
        "G()(al)"
        stack = ["G", "o", ]
        if the char before ) is letter:
        pop all the way till you find
        """
        stack = []
        
        
        for idx in range(len(command)):
            astr = ""
            if command[idx] == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                    stack.append("o")
                else: #  if it is a letter
                    while stack and stack[-1]!= "(":
                        astr += stack.pop()
                    if stack:
                        stack.pop()
                    for letter in astr[::-1]:
                        stack.append(letter)
            else:
                stack.append(command[idx])
        return "".join(stack)
                    
                    
                
            