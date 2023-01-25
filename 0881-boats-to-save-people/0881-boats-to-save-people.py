class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        start, end = 0, len(people)-1
        boat_count = 0
        
        while start < end:
            if people[start]+people[end] > limit:
                boat_count += 1
                end -= 1
            elif people[start]+people[end] <= limit:
                boat_count += 1
                start += 1
                end -= 1
        if start == end:
            boat_count += 1
        
        return boat_count 
                