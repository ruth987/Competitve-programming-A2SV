class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        bbbab =>  bbbb

        at every letter i will have two decisions:
            - whether to add the letter ot
            - not to add the letter
        at every step check if the string is palindromic or not
            - if it is update the length into something longer
        i can start checking from the start and the end 
        so basically i will have two parameters: startidx and endidx

        now let's change it into bottom up.

        """
        # n = len(s)

        # @cache
        # def dp(startidx, endidx): 
        #     #if the indexs are equal that means it is one letter 
        #     if startidx > endidx:
        #         return 0
        #     if startidx == endidx:
        #         return 1
        #     if s[startidx] == s[endidx]:
        #         return 2 + dp(startidx+1, endidx-1)
            
        #     return max(dp(startidx+1, endidx), dp(startidx, endidx-1)) 
        
        # return dp(0, n-1)
        n = len(s)
        dp = [[0]*n for _ in range(n)]

        # for one length palindromic strings
        for i in range(n):
            dp[i][i] = 1

        for startidx in range(n-1, -1, -1):
            for endidx in range(startidx+1, n):
                if s[startidx] == s[endidx]:
                    dp[startidx][endidx] = 2+dp[startidx+1][endidx-1]
                else:
                    dp[startidx][endidx] = max(dp[startidx+1][endidx], dp[startidx][endidx-1]) 
        
        return dp[0][n-1]