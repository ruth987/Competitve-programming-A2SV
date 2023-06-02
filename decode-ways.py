class Solution:
    def numDecodings(self, s: str) -> int:
        """
        so basically we have differnt ways of approach for two digits and one 
        digits
        bottom up: we can start from the start then assign the first as one
        we can decode the first number into one number
        for the second one: it depends on the first

        """
        dp = [0]* (len(s)+1)
        dp[0] = 1
        if s[0] != "0":
            dp[1] = 1
        else:
            dp[1] = 0 
        for i in range(2, len(s)+1):
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            if s[i-2:i] >= "10" and s[i-2:i] <="26":
                dp[i] += dp[i-2]
        return dp[-1]