class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        aset = set()
        row = len(grid)
        col = len(grid[0])
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    aset.add((r,c))
        # print(aset)
        count = 0
        def dfs(r,c):
            nonlocal count
            if r < 0 or r >= row or c < 0 or c >= col:
                return 
            if grid[r][c] == 0:
                return
            grid[r][c] = 0
            count += 1
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r, c+1)
            dfs(r, c-1)

        max_count = 0
        for ro in range(row):
            for co in range(col):
                if grid[ro][co] == 1:
                    dfs(ro,co)
                    max_count = max(max_count, count)
                    count = 0
        

        return max_count