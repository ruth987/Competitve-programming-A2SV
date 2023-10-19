class Solution:
    def countOrders(self, n: int) -> int:
        mul = 1
        for i in range(n):
            mul *= 2
        
        print(mul)
        
        return (factorial(n*2) // mul)% (10**9 + 7)