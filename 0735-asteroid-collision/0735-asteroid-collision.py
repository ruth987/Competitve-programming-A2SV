class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for idx in range(len(asteroids)):
            if not stack or asteroids[idx]>0 or stack[-1]<0: 
                stack.append(asteroids[idx])
            else:
                x = 0
                while stack and asteroids[idx]<0 and stack[-1]>0:
                    
                    if abs(asteroids[idx]) > stack[-1]:
                        stack.pop()
                        x = 1
                    elif abs(asteroids[idx]) < stack[-1]:
                        x = 0
                        break
                    else: #what if they are equal
                        x = 0
                        stack.pop()
                        break
                if x == 1:
                    stack.append(asteroids[idx])
        return stack

        