class Solution:
    def countPrimes(self, n: int) -> int:

        if n == 1 or n==0: return 0
        primes = [True] * (n+1)
        primes[0] = False
        primes[1] = False

        for idx in range(2, int(n**0.5)+1):
            if primes[idx]:
                for j in range(idx*idx, n, idx):
                    primes[j] = False
        
        count = 0
        for i in range(2, n):
            if primes[i]:
                count += 1
        
        return count