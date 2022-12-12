class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        the optimized using heap: should we use min heap or max heap?
        we can use minHeap then take the last two elements and collide them 
        then heappush the new element then heapify the minHeap again.
        """
        myStones = [-weight for weight in stones]
        heapq.heapify(myStones)
        
        while len(myStones) >= 2:
            s1 = heapq.heappop(myStones)
            s2 = heapq.heappop(myStones)
            if s2>s1:
                heapq.heappush(myStones, s1-s2)
        if not myStones:
            return 0
        return abs(myStones[0])
            
