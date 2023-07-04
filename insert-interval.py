class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        result.append(newInterval)
        return result
        
        """
        if the new interval appears in a way that it touches other intervals
        then we have to merge all the intervals that touch eachother.

        lets name the ones to be inserted as [x, y]
        we iterate through intervals till we find one that includes x
        then we keep going till we find the one that includes y then 
        we merge all the intervals up to that point 

        """