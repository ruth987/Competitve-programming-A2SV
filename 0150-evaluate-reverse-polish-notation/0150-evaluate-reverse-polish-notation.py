class Solution(object):
    def evalRPN(self, tokens):
        myops = {"+":(lambda x, y : x+y), "-":(lambda x, y : x-y), "*":(lambda x, y : x*y), "/": (lambda x, y : x/y)}
        stack = []
        
        for thing in tokens:
            if thing in myops:
                first = int(stack.pop())
                second = int(stack.pop())
                stack.append(int(myops[thing](second, first)))
            else:
                stack.append(thing)
        return stack.pop()
    