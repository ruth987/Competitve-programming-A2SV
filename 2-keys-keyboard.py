class Solution:
    def minSteps(self, n: int) -> int:
        """
        for n == 3 => AAA

        start:
        A
        2 - copy paste
        AA 
        3 - paste
        AAA
        can i do greedy?
        or simply a top down dp
        """
        @cache
        def dp(rem_amount, board):
            print(rem_amount)
            if rem_amount == n:
                return 0
            if rem_amount > n:
                return float('inf')

            cp, pt = float('inf'), float('inf')
            #if i copypaste
            cp = dp(rem_amount*2, rem_amount)+2 
            #if i paste
            if board:
                pt = dp(rem_amount + board, board)+1

            return min(cp, pt)

        
        return dp(1, 0)