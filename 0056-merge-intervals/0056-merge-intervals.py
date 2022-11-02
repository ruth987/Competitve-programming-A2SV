class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda item:item[0])
        stack = [intervals[0]]
        
        for idx in range(1,len(intervals)):
            if stack and stack[-1][1] >= intervals[idx][0]:
                s = stack.pop()
                stack.append([s[0],max(intervals[idx][1],s[1])])
            else:
                stack.append(intervals[idx])
        return stack
