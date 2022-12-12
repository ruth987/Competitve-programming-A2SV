class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        the optimized using heap: should we use min heap or max heap?
        we can use minHeap then take the last two elements and collide them 
        then heappush the new element then heapify the minHeap again.
        """
        stones = [-weight for weight in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            if s2>s1:
                heapq.heappush(stones, s1-s2)
        if not stones:
            return 0
        return abs(stones[0])
            
