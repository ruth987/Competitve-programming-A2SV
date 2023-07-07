class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        an island is ones connected 4 directionally
        we can do a dfs: 
        by iterating through the grid we can call our dfs function in each ones
        that arenot already visited by the island created with the other one 
        then we can count the number of islands when ever we call the function

        """
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def dfs(r,c):
            if r<0 or r==rows or c<0 or c==cols or (r,c) in visited or grid[r][c]=="0":
                return 

            visited.add((r,c))
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r, c)
                    count += 1

        return count