class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        find the kth smallest element
        [[1,5,9],
        [10,11,13],
        [12,13,15]]
        find the 8th smallest:
        we can have a max heap - with size o(n)
        we check if a number is smaller than the heap[0] if that is true
        we pop and push the new value that way the value at the front
        """
        rows = len(matrix)
        cols = len(matrix[0])
        heap = []
        for r in range(rows):
            for c in range(cols):
                if len(heap) < k:
                    heapq.heappush(heap, -matrix[r][c])
                else:
                    if -matrix[r][c] > heap[0]:
                        heapq.heappushpop(heap, -matrix[r][c])
        # print(heap)
        return -heap[0]