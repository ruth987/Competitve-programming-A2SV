class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        curr = ""
        
        for ch in path+"/":
            if ch == "/":
                if curr == "..":
                    if stack: 
                        stack.pop()
                elif curr != "." and curr != "":
                    stack.append(curr)
                curr = ""                        
            else:
                curr += ch
                
        return "/"+"/".join(stack)
            
        
