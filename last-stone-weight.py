class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -1*stones[i]
        heapq.heapify(stones)

        while len(stones) > 1:
            largest1 = -1*heapq.heappop(stones)
            largest2 = -1*heapq.heappop(stones)

            if largest1 > largest2:
                heapq.heappush(stones, -(largest1-largest2))
            elif largest2 > largest1:
                heapq.heappush(stones, -(largest2-largest1))
        
        if len(stones) == 1:
            return -stones[0]
        return 0