class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        let's first try to do it with a top down approach
        """
        def dfs(idx,buy):

            if(idx >= len(prices)):
                return 0
            
            if(dp[idx][buy] != -1):
                return dp[idx][buy]
            
            if(buy):
                profit = max(-prices[idx] + dfs(idx+1,0), 0 + dfs(idx+1,1))
                
            else:
                profit = max(prices[idx] + dfs(idx+2,1), 0 + dfs(idx+1,0))
                
            dp[idx][buy] = profit
            return dp[idx][buy]
        
        n = len(prices)
        dp = [[-1 for i in range(2)] for i in range(n)]
		
        return dfs(0,1)