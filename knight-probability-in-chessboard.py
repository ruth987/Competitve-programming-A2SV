class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        directions = [(2, -1), (2, 1), (1, -2), (-1, -2),
                    (-2, -1), (-2, 1), (-1, 2), (1, 2)]
        
        isValid = lambda r, c: not (r < 0 or r >=n or c < 0 or c >=n)

        @cache
        def dfs(r, c, moves):
            if not isValid(r,c):
                return 0
            if moves == 0:
                return 1

            count = 0
            for dr,dc in directions:
                row, col = r+dr, c+dc
                count += dfs(row, col, moves-1)
            
            return count
        
        res = dfs(row, column, k)

        return res/8**k