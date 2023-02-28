mydict = {}
class Solution:
    def fib(self, n: int) -> int:
        if n==1 or n==0:
            return n
        if n-1 in mydict:
            first = mydict[n-1]
        else:
            first = self.fib(n-1)
            mydict[n-1] = first
        if n-2 in mydict:
            second = mydict[n-2]
        else:
            second = self.fib(n-2)
            mydict[n-2] = second
        
        return first + second
        
        
        