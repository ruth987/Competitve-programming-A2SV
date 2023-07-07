class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        try it with bfs

        """
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        count = 0

        def isValid(r,c):
            if r<0 or r==rows or c < 0 or c == cols:
                return False
            return True

        def bfs(r,c):
            qu = deque()
            qu.append((r,c))

            while qu:
                length = len(qu)
                for i in range(length):
                    row,col = qu.popleft()
                    if not isValid(row,col) or (row,col) in visited  or grid[row][col]=="0": continue
                    visited.add((row,col))
                    qu.append((row+1, col))
                    qu.append((row-1, col))
                    qu.append((row, col+1))
                    qu.append((row, col-1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    count += 1
        return count