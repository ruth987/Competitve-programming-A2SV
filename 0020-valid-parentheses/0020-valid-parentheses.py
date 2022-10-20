class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bra in s:
            if bra in "{[(":
                stack.append(bra)
            else:
                if not stack:
                    return False
                else:
                    if bra == "]":
                        if stack[-1]=="[":
                            stack.pop()
                        else:
                            return False
                    elif bra == "}":
                        if stack[-1]=="{":
                            stack.pop()
                        else:
                            return False
                    else:
                        if stack[-1]=="(":
                            stack.pop()
                        else:
                            return False
        return len(stack)==0

