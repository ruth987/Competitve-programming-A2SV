class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        """
        max possible value
        [2,2,1,2,1]
        sort it 
        [1,1,2,2,2]
        if the value of the first isnot one reduce it to one 
        then make sure the second element is one or two


        """
        arr.sort()
        arr[0] = 1
        for idx in range(1, len(arr)):
            if arr[idx]-arr[idx-1] > 1:
                arr[idx] = arr[idx-1] + 1
        
        return arr[-1]