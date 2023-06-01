class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[0 for i in range(x)] for x in range(1, len(triangle)+1)]
        dp[-1] = triangle[-1]

        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(dp[i])):
                dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])
        
        return dp[0][0]




        print(dp)
        return 1