class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        """
        bricks = h[i+1]-h[i] or 1 ladder
        what is the furthest building index i can reach ?
        heights = [4,2,7,6,9,14,12]
        heap = [(2, 5), (4, 3), (5, 5)]
        minheap - (last_index, height_difference)

        i wanna use the bricks for the minimum ones and the ladder for the bigger ones
        """
        minheap = []
        n = len(heights)
        for idx in range(1, n):
            if heights[idx]-heights[idx-1] > 0:
                heapq.heappush(minheap, heights[idx]-heights[idx-1])
            if len(minheap) > ladders:
                diff = heapq.heappop(minheap)
                bricks -= diff
                if bricks < 0:
                    return idx-1

        return n-1