class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows = len(grid1)
        cols = len(grid1[0])

        def dfs(r, c, visited):
            if r < 0 or r == rows or c < 0 or c == cols or grid2[r][c] == 0 or (r,c) in visited:
                return True
            if grid1[r][c] == 0:
                return False
                
            visited.add((r,c))
            first = dfs(r-1, c, visited)
            second = dfs(r+1, c, visited)
            third = dfs(r, c+1, visited)
            fourth = dfs(r, c-1, visited)
            return first and second and third and fourth
            

        # iterate through the islands of grid2 and count those that are islands in g1
        aset = set()
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1 and (r,c) not in aset:
                    if dfs(r,c,aset):
                        count += 1
        return count