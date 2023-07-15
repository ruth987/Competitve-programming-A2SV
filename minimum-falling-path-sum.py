class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        @cache
        def dfs(r, c):
            if r == rows - 1:
                return matrix[r][c]


            min_sum = float('inf')
            for col in range(max(c - 1, 0), min(c + 2, cols)):
                min_sum = min(min_sum, dfs(r + 1, col) + matrix[r][c])

            return min_sum

        ans = float('inf')
        for c in range(cols):
            ans = min(ans, dfs(0, c))

        return ans