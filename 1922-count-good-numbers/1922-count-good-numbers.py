class Solution:
    def countGoodNumbers(self, n: int) -> int:
        """
        even index ==> even
        odd ==> prime
        """
        var = 10**9 + 7
        def fn(a, n):
          if (n == 0):
            return 1

          if (n % 2 == 0):
            return fn(a*a%var, n/2)

          return a * fn(a*a%var, (n-1)/2)
        
        if n == 1:
            return 5
        if n%2 != 0:
            evens = n//2 + 1
            odds = evens-1
        else: # for n is even
            evens = n//2
            odds = evens
        return fn(5, evens) * fn(4, odds)%(var)
    
    