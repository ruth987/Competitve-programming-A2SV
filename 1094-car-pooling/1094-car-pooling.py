class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # find the maximum of all the destinations
        # find minimum of all the starts
        max_des = -inf
        min_start = float('inf')
        
        for num_p, start, end in trips:
            max_des = max(max_des, end)
            min_start = min(min_start, start)

        # create an array with a size of their difference and initialize as zeros
        prefix = [0]*(max_des+1)
        # add numpassengers at the start and substract from the end
        for num_p, start, end in trips:
            print(start-1, end-1)
            prefix[start] += num_p
            prefix[end] -= num_p
        # calculate their prefix sum
        prefix = list(accumulate(prefix))
        # find the maximum value and compair with the capacity
        max_val = max(prefix)
        if max_val > capacity:
            return False
        return True