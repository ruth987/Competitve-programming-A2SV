class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # find the shortest path from the start of the grid to the end of the grid
        """
        we can use bfs to find the shortest path
        qu = deque([ (r, c)])

        we use the qu to store the next possible zero using 8 directional search
        qu can be initialized with (0, 0)
        """
        if grid[0][0]!=0:
            return -1
        rows = len(grid)
        cols = len(grid[0])

        def bfs_shortest_path(grid, start, end):
            queue = deque()
            queue.append((start[0], start[1], 1))
            grid[start[0]][start[1]] = 1

            while queue:
                row, col, dist = queue.popleft()
                if (row, col) == end:
                    return dist
                for d_row, d_col in [(1,0), (0,1), (0,-1), (-1,0), (-1,1), (-1,-1), (1,-1), (1,1)]:
                    n_row, n_col = row + d_row, col + d_col
 
                    if (0 <= n_row < len(grid) and 0 <= n_col < len(grid[0])) and grid[n_row][n_col] == 0:
                        grid[n_row][n_col] = 1
                        queue.append((n_row, n_col, dist + 1))

            return -1
        result = bfs_shortest_path(grid, (0, 0), (rows-1, cols-1))
        return result