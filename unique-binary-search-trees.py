class Solution:
    def numTrees(self, n: int) -> int:
        
        @cache
        def countTrees(n):
            if n <= 1:
                return 1
            ans = 0
            for rootNum in range(1, n+1):
                ans += (countTrees(rootNum-1) * countTrees(n-rootNum))
            
            return ans

        return countTrees(n)