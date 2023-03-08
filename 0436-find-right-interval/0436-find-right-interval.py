class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        new_i = [intervals[i][0] for i in range(len(intervals))]
        new_i.sort()
        for idx in range(len(intervals)):
            intervals[idx].append(idx)
            
        intervals.sort(key= lambda item: item[0])
        # print(intervals)
        ln = len(intervals)
        answer = [-1]*ln
        
        for interval in intervals:
            val = bisect_left(new_i,interval[1])
            if val < len(intervals):
                answer[interval[2]] = intervals[val][2]
                
        return answer