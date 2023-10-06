class Solution:
    def knightDialer(self, n: int) -> int:
        rows = 4
        cols = 3
        def isValid(r, c):
            if r<0 or r>=rows or c<0 or c>=cols:
                return False
            if r == rows-1 and (c==0 or c==cols-1):
                return False
            return True
        
        # start = (1, 0)
        directions =[(-1, -2), (-1, 2), (1, -2), (1, 2), (-2, 1), (-2, -1), (2, 1), (2, -1)]
        #n-1 jumps
        #how many numbers can i touch if i start from this
        cache = {}
        def dp(r, c, l):
            if not isValid(r, c):
                return 0
            if n == l:
                return 1
            if (r, c, l) in cache:
                return cache[(r, c, l)]
            v = 0
            for rw, co in directions:
                v += dp(r + rw, c + co, l + 1)

            cache[(r, c, l)] = v
            return cache[(r, c, l)]

        
        res = 0
        for r in range(rows):
            for c in range(cols):
                res += dp(r, c, 1)

        return res % (10**9 + 7)