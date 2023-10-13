class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        dp = [[1, 0, 0] for i in range(len(rating))]
        
        for i in range(1, len(rating)):
            for j in range(i):
                if rating[i] > rating[j]:
                    dp[i][1] += dp[j][0]
                    dp[i][2] += dp[j][1]
        
        a = sum(dp[i][2] for i in range(len(dp)))

        dp = [[1, 0, 0] for i in range(len(rating))]
        
        for i in range(1, len(rating)):
            for j in range(i):
                if rating[i] < rating[j]:
                    dp[i][1] += dp[j][0]
                    dp[i][2] += dp[j][1]
        
        b = sum(dp[i][2] for i in range(len(dp)))
        
        return a + b