class Solution:
    def countArrangement(self, n: int) -> int:
        mask = 0
        ans = 0
        path = []

        def backtrack(mask):
            nonlocal ans
            if len(path) == n:
                ans += 1
                return 
            
            for val in range(1, n+1):
                size = len(path) + 1
                if mask & (1 << val): continue

                if not size % val or not val % size:
                    path.append(val)
                    backtrack(mask | (1 << val))
                    path.pop()
        
        backtrack(0)
        return ans