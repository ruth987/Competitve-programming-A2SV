class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #decreasing monotonic stack
        stack = []
        answer = [0]*len(temperatures)
        
        for idx in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[idx]:
                s = stack.pop()
                answer[s] = idx-s
            stack.append(idx)
        return answer
            
        
            

        