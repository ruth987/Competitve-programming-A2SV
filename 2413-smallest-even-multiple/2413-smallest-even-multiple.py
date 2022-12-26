class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        x = lambda n: 2*n if n%2 != 0 else n
        return x(n)