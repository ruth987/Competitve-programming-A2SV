class Solution:
    def change(self, amount: int, coins: List[int]) -> int:        
        @functools.lru_cache(None)
        def foo(i, n):
            if i==0:        return 1
            if i<0 or n<0:  return 0
            return foo(i-coins[n], n) + foo(i, n-1)
        return foo(amount, len(coins)-1)