class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for size in asteroids:
            if stack and size < 0 and stack[-1] > 0:
                s = size + stack[-1]
                while stack and s<0 and stack[-1]>0 :
                    stack.pop()
                    if stack:
                        s = size + stack[-1]
                    else:
                        break
                if s<0:
                    stack.append(size)
                elif s > 0:
                    continue
                else:#s==0
                    stack.pop()      
            else:
                stack.append(size)
        return stack

        