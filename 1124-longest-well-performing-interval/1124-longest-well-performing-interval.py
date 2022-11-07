class Solution:
    def longestWPI(self, hours: List[int]) -> int: 
        #changing tiring days to +1 and the others to -1
        for idx in range(len(hours)):
            hours[idx] = 1 if hours[idx]>8 else -1
        
        #prefix sum of the hours array
        for idx in range(1, len(hours)):
            hours[idx] += hours[idx-1]
        
        #finding the longest well-performing interval
        max_len = 0
        mydict = {}
        for i,hr in enumerate(hours):
            if hr > 0:
                max_len = max(max_len, i+1)
            if hr-1 in mydict:
                max_len = max(max_len, i-mydict[hr-1])
            if hr not in mydict:
                mydict[hr] = i
                
        return max_len
