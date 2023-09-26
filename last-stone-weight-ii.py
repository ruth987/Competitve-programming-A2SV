class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
      """
      i need to consider all possible index pairs at every step
      solve 
       - napsack
       - partition list dp
      """
      n = len(stones)

      memo = {}
      def dp(idx, result):
        if (idx, result) in memo:
          return memo[(idx, result)]
        if idx >= n:
          return result if result >= 0 else float('inf')
        
        memo[(idx, result)] = min(dp(idx+1, result - stones[idx]),\
                                  dp(idx+1, result + stones[idx]) )

        return memo[(idx, result)]
      

      return dp(0, 0)