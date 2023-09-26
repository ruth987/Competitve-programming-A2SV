class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows = len(dungeon)
        cols = len(dungeon[0])

        def isValid(r, c):
            return 0 <= r < rows and 0 <= c < cols

        @cache
        def dp(r, c):
            if (r, c) == (rows - 1, cols - 1):
                return max(1, 1 - dungeon[r][c])

            min_health_on_exit = float('inf')

            for dr, dc in [(1, 0), (0, 1)]:
                row, col = r + dr, c + dc

                if isValid(row, col):
                    next_health = dp(row, col)
                    min_health_on_exit = min(min_health_on_exit, next_health - dungeon[r][c])

            return max(1, min_health_on_exit)

        return dp(0, 0)